from rest_framework import permissions
from rest_framework.views import Request, View


class IsColaboratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            return False

        return bool(request.user.is_colaborator)
