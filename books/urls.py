from django.urls import path
from . import views
from .views import BookView, BookViewDetail

urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/<int:pk>/", views.BookViewDetail.as_view())
]
