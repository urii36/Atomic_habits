from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать или удалять свои объекты, но не может видеть чужие.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить чтение всем.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить запись только владельцу объекта.
        return obj.user == request.user
