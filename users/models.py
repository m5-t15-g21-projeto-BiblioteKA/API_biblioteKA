from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_colaborator = models.BooleanField(null=True, default=False)
    can_locate = models.BooleanField(default=True)

    user_rents = models.ManyToManyField(
        "copies.Copy", through="rents.Rent", related_name="users_rents"
    )
