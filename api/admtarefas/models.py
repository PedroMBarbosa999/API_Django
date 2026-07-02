
# Create your models here.
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email