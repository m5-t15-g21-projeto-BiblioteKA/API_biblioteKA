from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Rent
from users.models import User
from .serializer import RentSerializer, RentDevolutionSerializer


# Create your views here.
class RentDetailView(generics.CreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer


class RentReturnView(generics.UpdateAPIView):
    serializer_class = RentDevolutionSerializer
    queryset = Rent.objects.all()


class historyView(generics.ListAPIView):
    serializer_class = RentSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        user_type = User.objects.get(id=id).is_superuser
        if user_type:
            return Rent.objects.all()
        else:
            user = User.objects.get(id=id)
            return Rent.objects.filter(user=user)
