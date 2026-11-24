# TODO: Demo Monitoring Infrastructure (Linux)

Small, AI-friendly increments. Demo runs **locally on the Cursor host** only.  
PRD: [requirements.md](./requirements.md)

Mark items `[x]` as you complete them.

---

## Phase 0 — Project initialization & basic UI

### 0.1 Repo skeleton
- [x] Create project root layout: `app/`, `agent/`, `tests/`, `docs/`, `.github/workflows/`
- [x] Add `README.md` with one-paragraph purpose + link to `docs/requirements.md`
- [x] Add `.gitignore` (Python, venv, `.env`, `__pycache__`, SQLite DB files)
- [x] **Security:** Ensure `.env` and any secret files are listed in `.gitignore`
- [x] **Docs:** Note in `README.md` that this is a local demo only

### 0.2 Python / Flask bootstrap
- [x] Create `requirements.txt` with Flask (pin a recent stable version)
- [x] Create minimal Flask app entry (`app/__init__.py` + `app/routes.py` or `app/main.py`)
- [x] Add a `/` route that renders a simple “Monitoring Demo” home page
- [x] Run/bind Flask app on `0.0.0.0:5777`
- [x] **Security:** Document that `0.0.0.0` exposes the demo on all interfaces; keep auth + agent token required
- [x] **Docs:** Add “Run locally” section to `README.md` (`python -m venv`, `pip install`, `flask run`)

### 0.3 Basic UI shell
- [x] Add `app/templates/base.html` (layout, nav placeholders)
- [x] Add `app/static/css/style.css` with a simple attractive look
- [x] Add placeholder pages: Dashboard, Server detail, Manage servers (static/empty content)
- [x] **Security:** No inline user-controlled HTML; use Jinja escaping by default
- [x] **Docs:** Document page map in `docs/ui.md` (Login → Dashboard → Detail → Manage)

---

## Phase 1 — Sign-in & unit tests

### 1.1 Config & secrets
- [ ] Add `.env.example` with `FLASK_SECRET_KEY=` and `ADMIN_PASSWORD=` (placeholders only)
- [ ] Load config from environment (no secrets in source)
- [ ] **Security:** Generate/require a strong `FLASK_SECRET_KEY`; never commit real `.env`
- [ ] **Docs:** Document required env vars in `README.md`

### 1.2 Password hashing
- [ ] Implement hash helper (Werkzeug `generate_password_hash` / `check_password_hash`)
- [ ] Seed or store default user `admin` with **hashed** password only
- [ ] **Security:** Never log or print the plain password; store hash only
- [ ] **Docs:** Note default username `admin` and that password is set via env at first run

### 1.3 Login / logout routes
- [ ] Add Login page template + POST handler
- [ ] On success, set session and redirect to Dashboard
- [ ] Add Logout route that clears session
- [ ] Protect Dashboard / Detail / Manage with a login-required check
- [ ] **Security:** Use Flask sessions; POST-only login; constant-time hash check via Werkzeug
- [ ] **Docs:** Update `docs/ui.md` with login flow

### 1.4 Auth unit tests
- [ ] Add `tests/` with pytest + Flask test client
- [ ] Test: valid `admin` login redirects to dashboard
- [ ] Test: invalid password stays on login / returns error
- [ ] Test: protected route redirects when logged out
- [ ] Test: password is stored hashed (not plaintext) in storage
- [ ] **Security:** Tests use a throwaway secret key and test password; no production secrets
- [ ] **Docs:** Add “Run tests” (`pytest`) to `README.md`

---

## Phase 2 — CI/CD (GitHub Actions)

### 2.1 Workflow skeleton
- [ ] Add `.github/workflows/ci.yml`
- [ ] Trigger on push and pull_request to main branches
- [ ] **Docs:** Add short “CI” note in `README.md` (what the workflow runs)

### 2.2 CI jobs (minimal)
- [ ] Job: checkout → setup Python → install deps → run `pytest`
- [ ] Optional: pin Python version (e.g. 3.11 or 3.12)
- [ ] **Security:** Do not inject real secrets into CI; use dummy `FLASK_SECRET_KEY` / test password in workflow `env`
- [ ] **Docs:** Document that CI is test-only (no deploy); local run remains the deployment path

---

## Phase 3 — Server registry (hostname)

### 3.1 Storage
- [ ] Choose SQLite (or a single JSON file) for server list
- [ ] Model/fields: `id`, `hostname`, `created_at` (minimal)
- [ ] **Security:** Validate hostname format (reject empty, control chars, overly long values)
- [ ] **Docs:** Document storage location and how to reset demo data

### 3.2 Manage servers UI
- [ ] List registered hostnames
- [ ] Add server form (hostname only)
- [ ] Remove server action
- [ ] **Security:** Require login; use POST for add/remove; CSRF protection (Flask-WTF or equivalent simple token)
- [ ] **Docs:** Update `docs/ui.md` for Manage servers

### 3.3 Server registry tests
- [ ] Test add valid hostname
- [ ] Test reject invalid/empty hostname
- [ ] Test remove server
- [ ] Test unauthenticated access denied
- [ ] **Security:** Confirm destructive actions require auth
- [ ] **Docs:** Mention registry tests under “Run tests”

---

## Phase 4 — Agent & CPU % ingestion

### 4.1 Agent (minimal)
- [ ] Create `agent/` script that reads local CPU % (e.g. `psutil`)
- [ ] Agent sends CPU % + hostname to Flask ingest endpoint (HTTP POST)
- [ ] **Security:** Shared demo token (`AGENT_TOKEN`) in header; reject requests without it
- [ ] **Docs:** Add `docs/agent.md` — install deps, set token, run agent on a host

### 4.2 Ingest API
- [ ] `POST /api/metrics` accepts hostname + cpu_percent
- [ ] Store latest CPU % per registered hostname
- [ ] Ignore or reject metrics for unknown hostnames (demo policy: only registered hosts)
- [ ] **Security:** Require `AGENT_TOKEN`; validate `cpu_percent` range (0–100); no arbitrary code execution
- [ ] **Docs:** Document ingest payload example in `docs/agent.md`

### 4.3 Agent / ingest tests
- [ ] Test ingest with valid token updates stored CPU %
- [ ] Test ingest without/invalid token returns 401/403
- [ ] Test invalid cpu_percent rejected
- [ ] **Security:** Cover token failure cases in CI
- [ ] **Docs:** Note agent tests in `README.md`

---

## Phase 5 — Dashboard, detail & auto-refresh

### 5.1 Dashboard (read-only)
- [ ] Show all servers with latest CPU % (or “—” if none yet)
- [ ] Link each row to Server detail
- [ ] **Security:** Read-only display; no forms that edit metrics
- [ ] **Docs:** Screenshot or short description in `docs/ui.md`

### 5.2 Server detail (read-only)
- [ ] Show hostname + current CPU %
- [ ] Handle missing server (404) and missing metrics gracefully
- [ ] **Security:** Login required; escaped output only
- [ ] **Docs:** Update `docs/ui.md`

### 5.3 Auto-refresh
- [ ] Add minimal JS (or meta refresh) to reload metrics every 5–10 seconds
- [ ] Prefer fetching a small JSON endpoint over full page reload if easy
- [ ] **Security:** JSON endpoint also requires session (or is safe read-only for logged-in users only)
- [ ] **Docs:** Document refresh interval in `docs/ui.md`

### 5.4 UI / metrics tests
- [ ] Test dashboard shows stored CPU % for a registered server
- [ ] Test detail page shows CPU %
- [ ] Test metrics JSON (if any) requires auth
- [ ] **Docs:** Final acceptance checklist mirror in `README.md`

---

## Phase 6 — Hardening & demo wrap-up

### 6.1 Security pass
- [ ] Confirm app binds to `0.0.0.0:5777`
- [ ] Confirm no plaintext passwords in repo, logs, or DB
- [ ] Confirm `.env.example` has no real secrets
- [ ] Confirm agent token not committed
- [ ] **Docs:** Add `docs/security.md` (auth, hashing, token, `0.0.0.0:5777` binding caveat, CSRF)

### 6.2 Documentation pass
- [ ] `README.md`: purpose, setup, run app, run agent, run tests, CI status badge (optional)
- [ ] Ensure `docs/requirements.md`, `docs/TODO.md`, `docs/ui.md`, `docs/agent.md`, `docs/security.md` are consistent
- [ ] **Docs:** Mark demo limitations (CPU % only, single admin, local only)

### 6.3 Acceptance (from PRD)
- [ ] Login works with `admin` + hashed password
- [ ] Can add server by hostname
- [ ] Can remove server
- [ ] Dashboard shows CPU % per server
- [ ] Server detail shows CPU %
- [ ] Values auto-refresh
- [ ] Monitoring views are read-only
- [ ] Runs on `0.0.0.0:5777` (Cursor host)
- [ ] CI workflow passes on GitHub Actions

---

## Suggested implementation order (summary)

1. Phase 0 — init + basic UI  
2. Phase 1 — sign-in + unit tests  
3. Phase 2 — GitHub Actions CI  
4. Phase 3 — add/remove servers by hostname  
5. Phase 4 — agent + CPU ingest  
6. Phase 5 — dashboard/detail + auto-refresh  
7. Phase 6 — security/docs/acceptance  

Work **one checkbox group at a time**; commit after each group when possible.
