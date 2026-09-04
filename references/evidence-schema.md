# AdvisorSignal packet schema v0.1

The validator accepts a JSON packet with these required top-level keys:

```json
{
  "schema_version": "0.1",
  "applicant": {"name": "...", "profile_sources": ["..."], "facts": []},
  "supervisor": {"name": "...", "institution": "...", "sources": ["..."]},
  "fit": {"score": 0, "confidence": "high", "breakdown": {}, "strengths": [], "gaps": []},
  "papers": [{"title": "...", "year": 2025, "url": "https://...", "reading_depth": "abstract"}],
  "deliverables": {"email": "...", "cv_emphasis": "...", "rp_alignment": "..."},
  "unknowns": []
}
```

Rules:

- `fit.score` is a prioritization aid, not an admissions probability.
- `fit.confidence` must be `high`, `medium`, or `low`.
- Each supervisor and paper must have at least one HTTP(S) source.
- `papers` must contain no more than two items.
- The validator rejects placeholder strings such as `TBD`, `TODO`, `your name`, and `example.com` in deliverables.
- The email must include a subject marker and a concrete ask, but the tool never sends it.
