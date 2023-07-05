from django.db import models


class Rent(models.Model):
    date_rent = models.DateField(auto_now_add=True)
    date_limit = models.DateField(null=True)
    date_devolution = models.DateField(null=True)

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
