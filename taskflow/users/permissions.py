from rest_framework import permissions
from taskflow.taskflow.users.enums import UserGroups


class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow HR users to access the view.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name=UserGroups.Manager.value).exists()
        )
