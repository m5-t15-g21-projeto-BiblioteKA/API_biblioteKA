from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from .serializers import UserSerializer


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
