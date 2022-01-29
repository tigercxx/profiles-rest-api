from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # allow users to see each other profile
        if request.method in permissions.SAFE_METHODS:  # GET/CREATE
            return True
        return obj.id == request.user.id  # everything else
