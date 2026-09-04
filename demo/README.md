# AdvisorSignal demo

This synthetic packet demonstrates the final audit shape without containing a real applicant's CV, email, or private data.

```powershell
python scripts/validate_packet.py demo/packet.json
```

The validator checks source presence, score bounds, paper count, a concrete doctoral ask, and common placeholders. It does not decide whether the research match is scientifically good; that remains an evidence and judgment task.
