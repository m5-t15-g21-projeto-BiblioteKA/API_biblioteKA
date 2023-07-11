from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer, UserStatusSerializer
from .permissions import IsAccountOwnerOrReadOnly, IsAccountOwnerOrAdmin, CreateOnly
from rents.models import Rent
from rents.serializer import RentSerializer


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateOnly]

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


class UserHistoryView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]

    serializer_class = RentSerializer

    def get_queryset(self):
        id = self.kwargs["pk"]
        user = User.objects.get(id=id)
        return Rent.objects.filter(user=user)
