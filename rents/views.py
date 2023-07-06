from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Rent
from .serializer import RentSerializer, RentDevolutionSerializer


# Create your views here.
class RentDetailView(generics.CreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer


class RentReturnView(generics.UpdateAPIView):
    serializer_class = RentDevolutionSerializer
    queryset = Rent.objects.all()
