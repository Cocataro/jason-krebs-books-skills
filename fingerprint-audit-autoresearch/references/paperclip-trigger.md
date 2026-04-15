# Paperclip Trigger — Scheduling the Quarterly Loop

Scheduled via Paperclip's CronCreate machinery. Fires every 90 days, dispatches a research subagent, creates a tracking issue.

## Trigger setup

Use the Paperclip `schedule` / CronCreate API. Target: fire at 09:00 UTC on the 1st of January, April, July, October.

Cron expression: `0 9 1 1,4,7,10 *`

### Trigger payload

```json
{
  "name": "fingerprint-audit-quarterly-research",
  "description": "Quarterly research dispatch for ai-fingerprint-audit maintenance",
  "cron": "0 9 1 1,4,7,10 *",
  "timezone": "UTC",
  "companyId": "6f61e9f7-6641-44a4-8a31-8d0699f3559d",
  "action": {
    "type": "create_issue",
    "issue": {
      "title": "Fingerprint audit research — Q[N] [YYYY]",
      "description": "Quarterly research dispatch. Dispatch a research subagent with the prompt in skills/fingerprint-audit-autoresearch/references/research-loop.md. Subagent produces proposed rubric diff. Thomas runs benchmark. Margaret approves. Board approves any threshold changes.",
      "priority": "normal",
      "assigneeAgentId": "<thomas-agent-id>",
      "labels": ["fingerprint-audit", "quarterly-research"]
    }
  }
}
```

## Setup steps

1. **Identify Thomas's agent ID** (from Paperclip agent list): `curl ...` — Thomas Albright's UUID.
2. **Register the cron trigger** via:
   ```bash
   curl -sS -X POST "https://paperclip-1gza.srv1377312.hstgr.cloud/api/triggers" \
     -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json" \
     -d @trigger-payload.json
   ```
3. **Verify the trigger** registered successfully.
4. **First manual run** — fire the trigger once by hand to validate the flow end-to-end before relying on the cron.

## Alternative: Claude Code `schedule` skill

If Paperclip's trigger infrastructure isn't the preferred path, Claude Code has a `schedule` skill for local cron-style scheduling. Less integrated but equivalently functional.

## Incident replay trigger (on-demand)

Incident replay runs on-demand, not on cron. Register a manual-invocation entry in the studio vault at `00-Meta/Operations/fingerprint-incident-replay.md` with step-by-step execution.

When an incident fires, Board or Margaret runs the replay process. No auto-trigger.

## Trigger maintenance

- **Quarterly** (first cycle after setup): verify cron fired on schedule, issue was created, research subagent dispatched, Thomas received and benchmarked.
- **If a cycle is missed:** fire manually; investigate why the trigger didn't run; fix; re-test.
- **Annually:** review whether 90-day cadence is right. If detector landscape moves faster, tighten to 60 days. If it stabilizes, relax to 120 days.

## Budget

- Cron trigger: free (infrastructure-level)
- Research subagent LLM tokens per cycle: ~$5
- Thomas's benchmark run: ~$2 in Pangram/GPTZero API calls
- **Total per cycle: ~$7**
- **Annual cost: ~$28**

Trivial compared to the value of a calibrated rubric.

## Fallback

If Paperclip's scheduled trigger infrastructure isn't available (or disabled for cost/security reasons):

1. Add a recurring calendar event on Nicole's calendar: "Fingerprint audit research — Q[N]"
2. Nicole manually runs the research dispatch (pastes the prompt from `research-loop.md` into a Claude conversation)
3. Nicole posts the output as a comment on a Paperclip issue manually
4. Thomas picks up as normal

Manual fallback works — the automation is convenience, not dependency.

## Confirmation of cron registration (Board note)

Before relying on the scheduled loop:
- [ ] Cron trigger payload submitted + verified in Paperclip
- [ ] Thomas agent ID confirmed in payload
- [ ] First manual run completed end-to-end
- [ ] Second automatic run verified to fire correctly
- [ ] Fallback-calendar event created in case of automation failure
- [ ] Board acknowledges the loop is live

## Logging

Every trigger fire logs:
- Fire timestamp
- Issue ID created
- Subagent dispatch success/failure
- Research deliverable received
- Benchmark run triggered + result
- Merge decision + git SHA

Log location: studio vault `00-Meta/Fingerprint-Research-Log/YYYY-QN/trigger-log.md`
