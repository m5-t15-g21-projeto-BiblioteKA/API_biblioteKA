from rest_framework import permissions
from .models import User
from rest_framework.views import Request, View


class IsAccountOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        user = User.objects.get(pk=view.kwargs["pk"])
        return bool(request.user == user)


class CreateOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_authenticated:
                return bool(request.user.is_colaborator)
            else:
                return False
        return True


class IsAccountOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        user = User.objects.get(pk=view.kwargs["pk"])

        if not request.user.is_authenticated:
            return False

        return bool(request.user.is_colaborator or request.user == user)
