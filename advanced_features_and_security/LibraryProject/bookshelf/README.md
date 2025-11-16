Permissions and Groups:

Groups:
- Viewers: can_view
- Editors: can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

Usage:
- Use @permission_required('relationship_app.can_edit', raise_exception=True)
  to restrict views to users with the correct permissions.
- Assign users to groups via Django Admin.