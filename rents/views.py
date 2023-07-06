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

    def get_queryset(self):
        rent_id = self.kwargs.get('pk')
        rent = get_object_or_404(Rent, id=rent_id)
        return Rent.objects.filter(id=rent_id)
