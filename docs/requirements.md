# PRD: Demo Monitoring Infrastructure (Linux Servers)

## 1. Overview

Local demo web app for internal L1/L2/L3 and application teams to view **live Linux server CPU %** without SSH login.

| Item | Detail |
|------|--------|
| Type | Demo only — run where Cursor is running |
| Stack | Python, Flask, simple attractive UI |
| Access | Read-only UI after sign-in |
| Collection | Lightweight **agent** on each monitored Linux host |

---

## 2. Problem

Today, checking live CPU usage means logging into each server. This demo replaces that with a central read-only UI.

---

## 3. Users

Internal teams only (L1, L2, L3, infrastructure, application development). Single shared `admin` account for the demo.

---

## 4. Goals / Success criteria

Demo is done when:

1. User signs in as `admin`.
2. User adds at least one Linux server by **hostname**.
3. Agent on that host reports CPU %.
4. Dashboard and server detail show **auto-refreshing** CPU % (no SSH required).
5. UI is read-only for monitoring data (no metric edits).

---

## 5. Out of scope (this demo)

- Memory, network, ports, disk, processes, alerts, multi-user roles
- Session timeout, change-password, SSO
- Cloud deploy, HA, encryption beyond hashed login password
- Non-Linux hosts

---

## 6. Features

### F1 — Read-only friendly UI

- Clean, simple screens for monitoring.
- Metrics and server inventory are view-only on dashboard/detail (no editing of CPU values).
- Server add/remove is allowed only on the manage-servers page (admin demo ops).

### F2 — Sign-in

- Default username: `admin`.
- Password stored as a **hash** (not plain text).
- No change-password flow and no session-timeout policy for the demo.
- After login, user lands on the dashboard.

### F3 — Add Linux servers

- Add a server with **hostname** only (required).
- List and remove servers from Manage Servers.
- App expects an **agent** on that host to push or expose CPU %.

### F4 — Live CPU % (auto-refresh)

- Dashboard: all servers with current CPU %.
- Server detail: hostname + current CPU %.
- UI **auto-refreshes** on a short interval (e.g. 5–10 seconds).

---

## 7. Screens (minimal)

1. **Login** — username + password  
2. **Dashboard** — server list + CPU %  
3. **Server detail** — one host + CPU %  
4. **Manage servers** — add (hostname) / remove  

---

## 8. Architecture (demo)

```
[Browser] → [Flask app on Cursor host] ← metrics ← [Agent on each Linux server]
```

- **Flask app**: auth, UI, server registry, show latest CPU %.
- **Agent**: runs on each monitored Linux host; reports CPU % to the Flask app (or app polls agent). Pick one simple approach for the demo.
- **Storage**: local file or SQLite for users (hashed password) and server hostnames + last CPU reading.

---

## 9. Tech notes

- Python 3 + Flask
- HTML/CSS (and minimal JS for auto-refresh)
- Password hashing via a standard library (e.g. `werkzeug` / `bcrypt`)
- Bind to `0.0.0.0` on port **5777**

---

## 10. Local run (minimal)

1. Install Python deps for the Flask app.
2. Start Flask app on the Cursor machine.
3. Install/start the agent on each Linux host to monitor (at least the local host for demo).
4. Open `http://<host>:5777` in a browser, sign in as `admin`, add hostname(s), confirm CPU % updates.

Default demo login:

- Username: `admin`
- Password: set once at setup; store only the hash in config/DB

---

## 11. Acceptance checklist

- [ ] Login works with `admin` + hashed password  
- [ ] Can add server by hostname  
- [ ] Can remove server  
- [ ] Dashboard shows CPU % per server  
- [ ] Server detail shows CPU %  
- [ ] Values auto-refresh without page reload / manual refresh  
- [ ] Monitoring views are read-only  
- [ ] Runs on `0.0.0.0:5777` (Cursor host) 
