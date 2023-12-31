from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/<int:pk>/status/", views.UserCanLocateView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/<int:pk>/history/", views.UserHistoryView.as_view()),
]
