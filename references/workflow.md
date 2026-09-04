# AdvisorSignal workflow details

## 1. Applicant evidence ledger

Create a ledger before searching:

| Field | Value | Source | Confidence | Notes |
|---|---|---|---|---|
| degree / date |  | `[PROFILE FACT]` | high |  |
| methods actually used |  | `[PROFILE FACT]` | high/medium | distinguish coursework from independent work |
| quantitative result |  | `[PROFILE FACT]` | high | preserve units and denominator |
| proposal question |  | `[PROFILE FACT]` | high | quote or paraphrase with a file anchor |
| target constraints |  | `[PROFILE FACT]` or `[ASSUMPTION]` |  |  |

Conflicts between CV, RP, and user instructions become `CONFLICT` items. Ask or flag them; never choose the more impressive version silently.

## 2. Supervisor evidence ledger

Use this order of evidence:

1. Official university or lab page for identity, role, group description, and recruitment language.
2. Official publication page, DOI record, or author-hosted paper page for paper metadata and contribution.
3. Reputable index or profile only to discover a source; verify the claim at tier 1 or 2.

Date-stamp volatile facts. “Accepting students”, funding, deadlines, and job openings expire; if no current source supports them, write `UNKNOWN` and use a neutral email question.

## 3. Fit reasoning

Use a matrix rather than a single intuition:

| Dimension | Weight | Evidence to cite |
|---|---:|---|
| Problem/topic | 30 | proposal question ↔ group question |
| Method/technical overlap | 30 | methods, datasets, modelling or experimental approach |
| Recent paper evidence | 20 | one or two current papers, not a publication count |
| Proposal feasibility with group | 10 | bounded extension and required resources |
| Practical fit | 10 | program, location, timeline or stated recruitment information |

For every score, write one positive evidence sentence and one limitation sentence. A high score with only a broad keyword match is invalid. Use `low` confidence when current primary evidence is missing.

## 4. Paper selection

Select at most two papers. A paper earns a place only if the applicant can say something specific after reading its abstract/full text:

- what problem it solves;
- what method or result connects to the applicant's proposal;
- what question or extension remains open.

Do not pretend to have read a full paper if only the abstract or metadata was available. Mark the reading depth.

## 5. Writing the packet

The inquiry email should be specific without becoming a mini-review. A good paragraph maps one applicant asset to one supervisor evidence point. After the proposal paragraph, include one natural adaptation sentence, for example by expressing willingness to shape the idea around the group's active questions and learn under the supervisor's guidance. Rewrite it to fit the particular group; never paste the same sentence into every message.

Use the applicant's exact verified name, degree, institution, methods, and results. Do not automatically normalize GPA, titles, or dates. If the user has explicitly chosen a representation such as `3.9/4.0`, record that it is a user-approved display choice and check it against the source.

## 6. Final audit

Before handoff:

- every paper title, author, year, DOI, and URL checked;
- every “recent/current/accepting” statement dated or removed;
- every applicant claim anchored to the CV/RP;
- no unsupported “perfect fit”, “top”, “guarantee”, or fabricated vacancy;
- one clear ask and no pressure to reply;
- no placeholder, accidental personal-data leakage, or attachment claim for a file not prepared;
- unknowns and suggested user review steps listed separately.

