from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .seriliazers import BookSerializer
from ..users.permissions import IsAccountOwner


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAccountOwner]


class BookViewDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
