from django.urls import path

from .views import RentDetailView


urlpatterns = [
    path("rents/", RentDetailView.as_view()),
    # path(
    #     "rents/<int:pk>/return",
    # ),
]
