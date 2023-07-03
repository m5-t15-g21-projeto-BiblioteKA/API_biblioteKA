from django.db import models


class Rent(models.Model):
    date_rent = models.DateTimeField(default=None)
    date_limit = models.DateTimeField(default=None)
    date_devolution = models.DateTimeField(default=None)

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        # related_name='rents',
        # null=True
    )

    copy = models.ForeignKey(
        'copies.Copy',
        on_delete=models.CASCADE,
        # related_name='rents',
        # null=True
    )
