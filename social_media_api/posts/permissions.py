from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Only the author of the object can edit or delete it.
    Others can only read.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only methods for anyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write methods are only allowed for the author
        return obj.author == request.user