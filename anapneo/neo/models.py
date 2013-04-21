from django.db import models
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
#    image = models.ImageField(upload_to=None, verbose_name="Image")
    