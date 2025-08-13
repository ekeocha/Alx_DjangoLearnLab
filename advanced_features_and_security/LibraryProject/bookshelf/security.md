# HTTPS & Security Hardening

- HTTPS enforced via `SECURE_SSL_REDIRECT = True`.
- HSTS enabled:
  - `SECURE_HSTS_SECONDS = 31536000`, `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`, `SECURE_HSTS_PRELOAD = True`.
- Secure cookies: `SESSION_COOKIE_SECURE = True`, `CSRF_COOKIE_SECURE = True`.
- Extra headers: `X_FRAME_OPTIONS = "DENY"`, `SECURE_CONTENT_TYPE_NOSNIFF = True`, `SECURE_BROWSER_XSS_FILTER = True`.
- Reverse proxy forwards HTTPS scheme via `X-Forwarded-Proto`; Django configured with `SECURE_PROXY_SSL_HEADER`.
- Production safety: `DEBUG = False`, `ALLOWED_HOSTS` set.

## Deployment
- TLS certificates installed with Let’s Encrypt (certbot).
- Nginx/Apache redirects all HTTP to HTTPS and proxies to the Django app.
- Static files served via Nginx `alias` after `collectstatic`.

## Notes
- Test HSTS on staging with a small duration (e.g., 300s) before enabling long-term in production.
- If using Content Security Policy, apply gradually and monitor browser console for blocked resources.
