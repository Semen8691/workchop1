
from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    name = models.CharField(
        max_length=50
    )

    email = models.EmailField(
        max_length=255,
        unique=True
    )


class CustomUser(User):
    age = models.PositiveIntegerField(

    )
# Create your models here.
