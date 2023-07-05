from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .models import Book
from .seriliazers import BookSerializer
from .permissions import IsColaboratorOrReadOnly


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaboratorOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
