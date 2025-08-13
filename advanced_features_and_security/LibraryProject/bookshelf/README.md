"""
Permissions & Groups Setup:
- Custom permissions are defined in Book.Meta.
- Groups:
    - Editors: can_create, can_edit
    - Viewers: can_view
    - Admins: all permissions
- Enforcement: @permission_required decorator in views
"""
