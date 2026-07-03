---
description: Create a Ralphthon @ICML welcome and orientation pack with attendee copy, QR/POP variants, operator checks, and next-step prompts.
---

# Ralphthon @ICML Welcome Pack

Produce a concise welcome/orientation pack for Ralphthon @ICML. Use public event facts and planning-safe context only.

## Preflight

1. Check whether the live Luma page is reachable: `https://luma.com/hjuo7auc`.
2. If browsing is available, verify the current title, venue, host, and any visible schedule or check-in guidance before writing public copy.
3. If browsing is unavailable, state that the pack is based on the embedded event facts in this command and the `hello-ralphthon-icml` skill.
4. Do not quote or reveal private Fireflies transcript content. Use only summarized planning signals: QR/POP/webpage access, guestbook engagement, coding-agent efficiency judging, auto-research skill/tutorial/wrapper, world-model sponsor narrative.

## Plan

Create one production-ready pack with:

1. Attendee welcome copy.
2. Orientation bullets for arrival and first action.
3. QR/POP copy variants.
4. Operator checklist.
5. Next-step prompts for the skill roadmap.

Prefer compact, event-floor usable copy over long explanation.

## Commands

Use these checks when the local environment allows them:

```bash
python3 scripts/validate_plugin.py
```

Optional live-page verification, only when network access is available:

```bash
python3 - <<'PY'
from urllib.request import urlopen

with urlopen("https://luma.com/hjuo7auc", timeout=10) as response:
    print(response.status)
    print(response.geturl())
PY
```

Use the verified Luma facts as the source of truth for attendee-visible details.

## Verification

Before finalizing, confirm:

- The event title is `Ralphthon @ICML "Auto Research" supported by Codex`.
- The venue is `NAVER D2SF 강남`, 서울 서초구 서초대로74길 14 삼성화재 서초타워 18층.
- The copy does not expose private transcript details.
- QR/POP copy includes a clear action: scan, check in, open the page, or leave a guestbook note.
- The pack points naturally toward `/auto-research` and `/world-model-ideation` as follow-up workflows.

## Summary

Return the result in this format:

```md
## Ralphthon @ICML Welcome Pack

### Attendee Welcome
<short copy>

### Orientation
- <arrival/check-in/location/action bullets>

### QR/POP Copy
- Short: <copy>
- Medium: <copy>
- Operator: <copy>

### Operator Checklist
- <checks>

### Next Prompts
- /auto-research: <prompt>
- /world-model-ideation: <prompt>
```

## Next Steps

- If the user wants attendee-facing assets, adapt the QR/POP section into print-ready signage copy.
- If the user wants workshop content, route to `/auto-research`.
- If the user wants sponsor or brand narrative, route to `/world-model-ideation`.
