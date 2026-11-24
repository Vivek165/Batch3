# UI page map

Phase 0 shell for PulseMonitor. All dynamic data is placeholder until later phases.

## Flow

```
Home (/) → Dashboard (/dashboard) → Server detail (/servers/<hostname>)
                ↘ Manage servers (/servers)
```

Login will sit in front of Dashboard / Detail / Manage in Phase 1.

| Route | Page | Status |
|-------|------|--------|
| `/` | Home — “Monitoring Demo” intro | Live (static) |
| `/dashboard` | Dashboard — server list + CPU % | Placeholder |
| `/servers/<hostname>` | Server detail — hostname + CPU % | Placeholder (`hostname` Jinja-escaped) |
| `/servers` | Manage servers — add/remove hostname | Placeholder |
| Login | Sign-in as `admin` | Not built yet |

## Security (UI)

- Templates use Jinja2 auto-escaping; do not pipe user input through `|safe`.
- No inline rendering of unsanitized hostnames or metrics.
- Binding: `0.0.0.0:5777` (see README security note).
