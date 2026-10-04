# API Data Collection Pipeline

Level: 1 — Python, Data & Automation

Skills: Python, a staged ingest, validation

Ingest already-fetched JSON records (no live HTTP). Summarize `latency_ms` by `endpoint`. Missing numbers are skipped.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.
