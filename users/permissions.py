from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """Класс для определения permissions, при принадлежности к группе 'moderator'."""
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
