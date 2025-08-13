"""
Permissions & Groups Setup:
- Custom permissions are defined in Book.Meta.
- Groups:
    - Editors: can_create, can_edit
    - Viewers: can_view
    - Admins: all permissions
- Enforcement: @permission_required decorator in views
"""

# Security Measures

- **Settings**: DEBUG=False in production; ALLOWED_HOSTS set; CSP via django-csp; X_FRAME_OPTIONS=DENY; SECURE_* headers; CSRF/SESSION cookies set Secure (HTTPS only).
- **Templates**: All POST forms include `{% csrf_token %}`; auto-escaping is on; user content is never marked `|safe`.
- **Views**: Use Django ORM or parameterized queries; user input validated via Forms; destructive actions (delete) only accept POST.
- **Testing**: Manual tests for CSRF (403 without token), XSS (no script execution), SQLi (queries are safe), response headers verified in browser tools.
