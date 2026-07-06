
# Create your models here.
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    status = models.IntegerField(choices=[(0, 'Pending'), (1, 'In Progress'), (2, 'Completed')], default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title