from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core import validators
from datetime import datetime

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(max_length=100)
    display_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100, blank=True, verbose_name="First Name")
    last_name = models.CharField(max_length=100, blank=True, verbose_name="Last Name")
    city = models.CharField(max_length=40, blank=True, verbose_name="City")
    country = models.CharField(max_length=40, blank=True, verbose_name="Country")
    lat = models.CharField(max_length=20, blank=True, verbose_name="Latitude")
    lon = models.CharField(max_length=20, blank=True, verbose_name="Longitude")


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'email')
