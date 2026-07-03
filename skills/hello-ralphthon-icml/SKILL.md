---
name: hello-ralphthon-icml
description: Welcome and orient Ralphthon @ICML attendees, operators, sponsors, and QR/POP traffic. Use when the user asks for Ralphthon ICML onboarding, attendee welcome copy, event orientation, QR or POP copy, guestbook engagement, hackathon context, Codex skill surface framing, or `/hello-ralphthon-icml`.
metadata:
  priority: 9
  docs:
    - "https://luma.com/hjuo7auc"
  pathPatterns:
    - "README.md"
    - "commands/hello-ralphthon-icml.md"
    - "skills/hello-ralphthon-icml/SKILL.md"
    - "**/luma*"
    - "**/guestbook*"
    - "**/qr*"
    - "**/pop*"
  promptSignals:
    - "Ralphthon @ICML"
    - "Ralphthon ICML onboarding"
    - "attendee welcome"
    - "event orientation"
    - "QR copy"
    - "POP copy"
    - "guestbook"
    - "Auto Research"
    - "world model"
    - "/hello-ralphthon-icml"
  keywords:
    - "QR코드"
    - "POP"
    - "IR퍼블릭덱"
    - "해커톤"
    - "월드모델"
    - "오토리서치"
---

# Hello Ralphthon @ICML

Use this skill to produce a concise welcome and orientation pack for Ralphthon @ICML: attendee-facing copy, operator briefing, QR/POP text, and next-step prompts that move people from arrival into the Ralph Loop.

## Event Facts

- Title: `Ralphthon @ICML "Auto Research" supported by Codex`
- Luma: `https://luma.com/hjuo7auc`
- Venue: `NAVER D2SF 강남`, 서울 서초구 서초대로74길 14 삼성화재 서초타워 18층
- Host/calendar: Team Attention / Goobong Jeong
- Strategic arc: hello and onboarding first, then auto-research, then world-model ideation.

## Operating Context

- Treat QR, POP, webpage access, and guestbook prompts as engagement surfaces.
- Frame the hackathon around coding-agent efficiency and practical research acceleration.
- Use summarized planning context only; do not expose raw meeting transcripts or private notes.
- When possible, verify the live Luma page before finalizing public copy.

## Output Shape

Return a compact pack with:

1. Attendee welcome message.
2. Event orientation bullets: what this is, where to go, what to do first.
3. QR/POP copy variants: short, medium, and operator-facing.
4. Host/operator checklist.
5. Suggested next prompts for `/auto-research` and `/world-model-ideation`.

Keep copy production-ready, bilingual when useful, and specific to Ralphthon @ICML.
