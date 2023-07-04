from django.db import models


class Rent(models.Model):
    date_rent = models.DateTimeField(auto_now_add=True)
    date_limit = models.DateTimeField(null=True)
    date_devolution = models.DateTimeField(null=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        # related_name='rents',
        # null=True
    )

    copy = models.ForeignKey(
        "copies.Copy",
        on_delete=models.CASCADE,
        # related_name='rents',
        # null=True
    )
