from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Fruits(models.Model):
    name = models.CharField(max_length=200)
    benefit = models.CharField(max_length=200)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ApiUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)