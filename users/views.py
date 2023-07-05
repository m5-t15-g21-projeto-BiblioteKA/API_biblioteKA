from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer, UserStatusSerializer
from rest_framework import generics
from .permissions import IsAccountOwnerOrReadOnly


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCanLocateView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = UserStatusSerializer

    def get_queryset(self):
        user_pk = self.kwargs["pk"]
        get_object_or_404(User, pk=user_pk)

        return User.objects.filter(pk=user_pk)
