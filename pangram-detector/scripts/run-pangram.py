#!/usr/bin/env python3
"""
Run Pangram AI-detection on a manuscript chapter.

Usage:
  python run-pangram.py --input path/to/Ch-NN.md --output path/to/detector-runs/Ch-NN-YYYYMMDD-HHMM.json

Reads the markdown file, strips YAML frontmatter, posts the body to Pangram's
/v3 AI-detection endpoint, writes the raw response + derived verdict to --output,
prints a one-line summary, exits 0 (PASS), 1 (FAIL), or 2 (WARN).

Env: PANGRAM_API_KEY must be set (Paperclip secret store).

Board SOP 2026-04-23: every chapter runs this at the post-revision, pre-line/copy gate.
Margaret will not mark ship-ready without a clean verdict artifact in Detector-Runs/.
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    sys.stderr.write("ERROR: `requests` library not installed. Run: pip install requests\n")
    sys.exit(3)

PANGRAM_URL = "https://text.api.pangram.com/v3"
FRACTION_AI_CEILING = 0.10
HUMAN_LABEL = "Human"
AI_ASSISTED_LABEL = "AI-Assisted"
HIGH_CONFIDENCE = "High"
AI_GENERATED_WINDOW_LABEL = "AI-Generated"


def strip_frontmatter(text: str) -> str:
    """Remove a leading YAML frontmatter block delimited by --- lines."""
    if not text.startswith("---"):
        return text
    parts = re.split(r"(?m)^---\s*$", text, maxsplit=2)
    if len(parts) >= 3:
        return parts[2].lstrip("\n")
    return text


def current_sha(manuscript_file: Path) -> str:
    """Return the git SHA of the repo containing manuscript_file, or empty string."""
    try:
        repo_root = subprocess.run(
            ["git", "-C", str(manuscript_file.parent), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        sha = subprocess.run(
            ["git", "-C", repo_root, "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        return sha
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def call_pangram(text: str, api_key: str, retries: int = 2) -> dict:
    """POST text to Pangram /v3. Retry on 5xx up to `retries` times."""
    headers = {"Content-Type": "application/json", "x-api-key": api_key}
    body = {"text": text, "public_dashboard_link": False}
    last_err = None
    for attempt in range(retries + 1):
        try:
            resp = requests.post(PANGRAM_URL, headers=headers, json=body, timeout=120)
        except requests.exceptions.RequestException as e:
            last_err = f"request exception: {e}"
            if attempt < retries:
                time.sleep(60)
                continue
            raise SystemExit(f"Pangram API unreachable after {retries + 1} attempts: {last_err}")
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 401:
            raise SystemExit(f"Pangram 401 — API key invalid or out of credit. Rotate via Board. Body: {resp.text[:300]}")
        if resp.status_code == 400:
            raise SystemExit(f"Pangram 400 — malformed request. Body: {resp.text[:300]}")
        if resp.status_code >= 500 and attempt < retries:
            last_err = f"5xx {resp.status_code}: {resp.text[:200]}"
            time.sleep(60)
            continue
        raise SystemExit(f"Pangram unexpected status {resp.status_code}: {resp.text[:300]}")
    raise SystemExit(f"Pangram retry loop exhausted: {last_err}")


def compute_verdict(pangram: dict) -> dict:
    """Apply Board-canonical pass/fail rules to a Pangram response."""
    prediction_short = pangram.get("prediction_short", "")
    fraction_ai = float(pangram.get("fraction_ai", 1.0))
    fraction_ai_assisted = float(pangram.get("fraction_ai_assisted", 0.0))
    fraction_human = float(pangram.get("fraction_human", 0.0))
    windows = pangram.get("windows", []) or []

    high_conf_ai_windows = [
        w for w in windows
        if w.get("label") == AI_GENERATED_WINDOW_LABEL and w.get("confidence") == HIGH_CONFIDENCE
    ]

    reasons = [
        f"prediction_short={prediction_short!r}",
        f"fraction_ai={fraction_ai:.3f}",
        f"fraction_ai_assisted={fraction_ai_assisted:.3f}",
        f"fraction_human={fraction_human:.3f}",
        f"high_confidence_AI_windows={len(high_conf_ai_windows)}",
    ]

    # FAIL takes precedence
    if prediction_short in ("AI", "Mixed"):
        return {"status": "FAIL", "reasons": reasons + [f"prediction_short={prediction_short!r} is a publish-blocker"], "flagged_windows": high_conf_ai_windows}
    if fraction_ai >= FRACTION_AI_CEILING:
        return {"status": "FAIL", "reasons": reasons + [f"fraction_ai>={FRACTION_AI_CEILING}"], "flagged_windows": high_conf_ai_windows}
    if high_conf_ai_windows:
        return {"status": "FAIL", "reasons": reasons + [f"{len(high_conf_ai_windows)} high-confidence AI windows"], "flagged_windows": high_conf_ai_windows}

    if prediction_short == HUMAN_LABEL:
        return {"status": "PASS", "reasons": reasons, "flagged_windows": []}
    if prediction_short == AI_ASSISTED_LABEL:
        return {"status": "WARN", "reasons": reasons + ["requires Eleanor sign-off per Board SOP"], "flagged_windows": []}

    return {"status": "FAIL", "reasons": reasons + [f"unrecognized prediction_short={prediction_short!r}"], "flagged_windows": high_conf_ai_windows}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Pangram AI-detection on a manuscript chapter.")
    parser.add_argument("--input", required=True, help="Path to chapter markdown file.")
    parser.add_argument("--output", required=True, help="Path to write detector-run JSON artifact.")
    parser.add_argument("--skip-frontmatter", default=True, type=lambda v: str(v).lower() not in ("false", "0", "no"), help="Strip YAML frontmatter from input (default: true).")
    args = parser.parse_args()

    api_key = os.environ.get("PANGRAM_API_KEY")
    if not api_key:
        sys.stderr.write("ERROR: PANGRAM_API_KEY env var not set. Get it from Paperclip secret store.\n")
        return 3

    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()
    if not input_path.is_file():
        sys.stderr.write(f"ERROR: input file does not exist: {input_path}\n")
        return 3
    output_path.parent.mkdir(parents=True, exist_ok=True)

    raw = input_path.read_text(encoding="utf-8")
    body = strip_frontmatter(raw) if args.skip_frontmatter else raw
    word_count = len(body.split())
    if word_count < 100:
        sys.stderr.write(f"ERROR: chapter body below 100 words after frontmatter strip (got {word_count}). Suspicious. Aborting.\n")
        return 3

    sha = current_sha(input_path)

    pangram = call_pangram(body, api_key)
    verdict = compute_verdict(pangram)

    artifact = {
        "chapter_file": str(input_path),
        "chapter_sha": sha,
        "chapter_word_count": word_count,
        "run_at": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "pangram_raw": pangram,
        "verdict": verdict,
        "ship_ready_gate": "CLEARED" if verdict["status"] == "PASS" else ("WARN_REVIEW" if verdict["status"] == "WARN" else "BLOCKED"),
    }

    output_path.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

    summary = f"{verdict['status']} | file={input_path.name} | fraction_ai={pangram.get('fraction_ai'):.3f} | prediction={pangram.get('prediction_short')!r} | artifact={output_path}"
    print(summary)

    if verdict["status"] == "PASS":
        return 0
    if verdict["status"] == "WARN":
        return 2
    return 1


if __name__ == "__main__":
    sys.exit(main())
