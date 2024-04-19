from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """Класс для определения permissions, при принадлежности к группе 'moderator'."""
    message = 'Для использования, нужно быть модератором.'

    def has_permission(self, request, view):
        """Метод проверки принадлежности к группе 'moderator'."""
        if request.user.groups.filter(name='moderator').exists():
            return True


class IsOwner(BasePermission):
    """Класс для определения permissions, при принадлежности к группе 'owner'."""
    message = 'Для использования, нужно быть владельцем.'

    def has_object_permission(self, request, view, obj):
        """Метод для проверки принадлежности к группе 'owner'."""
        if request.user == obj.owner:
            return True
