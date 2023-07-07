from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .models import Rent
from .serializer import RentSerializer, RentDevolutionSerializer


class RentDetailView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Rent.objects.all()
    serializer_class = RentSerializer


class RentReturnView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Rent.objects.all()
    serializer_class = RentDevolutionSerializer
