from django.shortcuts import render
from rest_framework import generics

from .models import Rent
from .serializer import RentSerializer


# Create your views here.
class RentDetailView(generics.CreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
