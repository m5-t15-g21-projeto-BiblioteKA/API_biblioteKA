from django.urls import path

from .views import RentDetailView, RentReturnView, historyView


urlpatterns = [
    path("rents/", RentDetailView.as_view()),
    path(
        "rents/<int:pk>/return/", RentReturnView.as_view()
    ),
    path("users/<int:pk>/history/", historyView.as_view()),
]
