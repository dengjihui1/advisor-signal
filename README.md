# AdvisorSignal

![Jihui](assets/brand/jihui-wordmark.png)

> A good PhD email is not “Dear Professor, I like your work.” It is a small, traceable research conversation.

AdvisorSignal turns a CV and research proposal into an evidence-grounded supervisor outreach packet:

`CV + RP → research representation → supervisor shortlist → fit evidence → 1–2 paper notes → tailored CV/RP positioning → complete inquiry email → audit`

## Why it is not another cover-letter generator

- It ranks supervisors before writing prose, so the email is downstream of a research decision.
- It requires official/primary evidence for supervisor identity, research direction, papers, and current recruitment claims.
- It exposes strengths, gaps, confidence, and unknowns instead of hiding them behind a single “fit score”.
- It selects no more than two papers and forces a method-level connection plus an honest question.
- It drafts only. It never sends an email or uploads a user's CV/RP.

## Quick start

```powershell
python scripts/validate_packet.py demo/packet.json
```

Use `$advisor-signal` with a local CV and one or more research proposals. The agent should first return a profile ledger and ranked supervisor cards. After the user selects a supervisor, it creates the target-specific material packet described in [SKILL.md](SKILL.md).

## Output structure

Each approved supervisor receives six reviewable files: fit card, paper notes, CV emphasis, RP alignment, inquiry email, and audit. The evidence schema is documented in [references/evidence-schema.md](references/evidence-schema.md).

## Safety and honesty

Local files stay local by default. Current vacancies, funding, deadlines, and “accepting students” claims are volatile and must be dated or marked unknown. A high fit score is a prioritization aid, not an admission probability. The final email must be reviewed by the applicant before sending.

## Research direction

The project treats supervisor outreach as an evidence alignment problem: can an agent preserve the applicant's actual evidence while finding a specific, defensible conversation with a research group? The most important evaluation is not email fluency; it is source accuracy, fit-reasoning usefulness, unsupported-claim rate, and whether applicants can explain why each target is worth contacting.
