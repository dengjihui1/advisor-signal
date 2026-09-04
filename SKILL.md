---
name: advisor-signal
description: Build an evidence-grounded PhD supervisor matching and outreach packet from a user's CV and research proposal. Use when the user wants to find suitable supervisors, compare research fit, select papers, tailor application materials, or draft a complete supervisor inquiry email; do not send emails or invent admissions facts.
---

# AdvisorSignal

AdvisorSignal turns a CV and one or more research proposals into a traceable supervisor-outreach packet. Its product is not a generic cover-letter generator: it creates a ranked shortlist, an evidence-backed fit map, selected paper notes, tailored CV/RP positioning, and a complete draft email that a person can review and send.

## Non-negotiable boundaries

- Read CV/RP files locally by default. Never upload them to the Skill package, a public repository, or a third-party service.
- Do not send email, submit an application, contact a professor, or claim that a position is open without explicit user action and a current source.
- Separate `[PROFILE FACT]`, `[LIVE SOURCE]`, `[INFERENCE]`, `[ASSUMPTION]`, and `[RECOMMENDATION]` in the working packet.
- Never fabricate a professor's paper, lab priority, funding, vacancy, admission requirement, name, title, or email address. If a source is missing, mark the field `UNKNOWN`.
- A match score prioritizes research time; it is not a probability of admission and must include a breakdown and confidence.
- Produce a shortlist first. Generate a final tailored CV/RP and inquiry letter only after the user selects or approves the target supervisor.

## Operating workflow

1. **Intake the applicant** — extract education, methods, projects, results, proposal questions, preferred degree/program, timeline, geography, constraints, and contact details. Preserve the source wording and record conflicts instead of silently fixing them.
2. **Represent research fit** — reduce each proposal to problem, object/system, method, evidence, expected contribution, and boundary. Extract reusable method keywords and adjacent directions; do not collapse a novel proposal into a broad label such as “AI interested”.
3. **Discover supervisors** — search official university/lab pages, official profiles, and primary paper pages first. Record source URL, access date, current role, research themes, recent work, group status, and uncertainty. Use secondary sources only as leads.
4. **Rank candidates** — score each candidate with a visible breakdown: problem/topic 30, method/technical overlap 30, recent paper evidence 20, proposal feasibility with the group 10, and practical fit 10. Apply confidence (`high`, `medium`, `low`) and a hard warning when the evidence is thin or stale.
5. **Create a decision card** — for each top candidate show: strongest overlap, meaningful gap, one proposed conversation point, two evidence links, why the applicant is credible, what remains unknown, and a reason to contact now. Do not hide a weak fit behind a high total score.
6. **Select papers** — choose at most two papers that are directly relevant and defensible. Prefer recent work that reveals the group's current method or open question. For each paper record title, authors, year, DOI/official URL, one-sentence contribution, method-level connection, and one honest question the applicant can ask.
7. **Tailor materials** — create a target-specific CV emphasis map and RP alignment memo before prose. Keep every achievement traceable to the CV and every proposed extension clearly labeled as a proposal, not prior work. If a Word document is requested, use Times New Roman and 1.5 line spacing unless the user asks otherwise.
8. **Draft the inquiry letter** — write a concise subject and complete email: identity/current status, precise research fit, one or two paper references, the applicant's relevant evidence, a bounded proposed direction, a natural sentence showing willingness to adapt to the group's priorities, and a low-pressure question about PhD opportunities. Avoid flattery, paper-title dumping, generic “your esteemed lab”, and claims of certainty.
9. **Audit before handoff** — run the packet validator, check every external fact has a source, check names/titles/dates/links, check no unsupported superlatives, check the email has no placeholder, and list unknowns. Output drafts only; never transmit them.

## Deliverables

For each approved supervisor, produce:

- `01-profile-and-fit.md` — source table, score breakdown, confidence, gaps, and decision card.
- `02-paper-notes.md` — no more than two source-grounded paper notes.
- `03-cv-emphasis.md` — what to foreground, compress, or leave unchanged, without inventing experience.
- `04-rp-alignment.md` — overlap, adaptation boundary, and questions for discussion.
- `05-inquiry-email.md` — subject plus complete email draft.
- `06-audit.md` — evidence ledger, unknowns, risk flags, and review checklist.

Read [references/workflow.md](references/workflow.md) for the detailed research and writing protocol. Read [references/evidence-schema.md](references/evidence-schema.md) when creating or validating structured packets. Use `scripts/validate_packet.py` for the final machine-checkable audit.

