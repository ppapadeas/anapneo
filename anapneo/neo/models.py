from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core import validators


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


class Neo(models.Model):
    user = models.ForeignKey(User)
    score = models.PositiveIntegerField(verbose_name="Score (%)")
    observation_date = models.DateTimeField(verbose_name="Observation Date")
    position_ra = models.CharField(max_length=100, verbose_name="R.A.")
    position_dec = models.CharField(max_length=100, verbose_name="Declination")
    magnitude = models.CharField(max_length=100, verbose_name="Magnitude")
    updated =  models.DateTimeField(max_length=100, verbose_name="Latest Observation")
    note = models.TextField(max_length=300, verbose_name="Notes")
    num_obs = models.PositiveIntegerField(verbose_name="Number of Observations")
    arc = models.FloatField(verbose_name="Arc")
    nominal_h = models.FloatField(verbose_name="Nominal H")
    image = models.ImageField(upload_to='.', verbose_name="Image")
