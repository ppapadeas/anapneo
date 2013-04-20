from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100, default='NULL')
    last_name = models.CharField(max_length=100, default='NULL')
    city = models.CharField(max_length=40, default='NULL')
    country = models.CharField(max_length=40, default='NULL')
    lat = models.CharField(max_length=20, default='NULL')
    lon = models.CharField(max_length=20, default='NULL')
