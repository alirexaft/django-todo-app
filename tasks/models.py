from django.db import models
from accounts.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    description = models.TextField(max_length=1500, blank=True)

    date_publish = models.TimeField(auto_now_add=True, blank=True)

    is_complete = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title
