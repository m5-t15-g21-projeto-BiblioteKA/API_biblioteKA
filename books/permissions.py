from rest_framework import permissions


class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permite a leitura (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Permite apenas criação (POST) se o usuário for superusuário
        return request.user and request.user.is_superuser
