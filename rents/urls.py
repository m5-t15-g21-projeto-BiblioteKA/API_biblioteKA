from django.urls import path
from .views import RentDetailView, RentReturnView


urlpatterns = [
    path("rents/", RentDetailView.as_view()),
    path("rents/<int:pk>/return/", RentReturnView.as_view()),
]
