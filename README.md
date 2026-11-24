# PulseMonitor — Demo Monitoring Infrastructure (Linux)

Local demo web app for internal L1/L2/L3 teams to view live Linux server **CPU %** without SSH. Spec: [docs/requirements.md](docs/requirements.md). Task list: [docs/TODO.md](docs/TODO.md).

**This is a local demo only** (run on the Cursor host). It is not production-ready.

## Security note (binding)

The app listens on **`0.0.0.0:5777`**, which exposes it on all network interfaces. Use only on trusted networks. Sign-in and an agent token will be required in later phases; do not leave an unauthenticated demo reachable on untrusted networks.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Open `http://<host>:5777` (or `http://127.0.0.1:5777` on this machine).

## Project layout

| Path | Purpose |
|------|---------|
| `app/` | Flask UI |
| `agent/` | Metrics agent (later phase) |
| `tests/` | Unit tests (later phase) |
| `docs/` | PRD, TODO, UI notes |
| `.github/workflows/` | CI (later phase) |
