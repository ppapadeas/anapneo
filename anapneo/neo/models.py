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

# About the fields of Neo Table ask Giannis Belias mailto: yiannisbe@gmail.com
class Neo(models.Model):
    user = models.ForeignKey(User)
    observation_date = models.DateTimeField(verbose_name="Observation Date")
    position_ra = models.CharField(max_length=100, verbose_name="R.A.")
    position_dec = models.CharField(max_length=100, verbose_name="Declination")
    magnitude = models.CharField(max_length=100, verbose_name="Magnitude")
    exposure = models.FloatField(verbose_name="Exposure Time (sec)")
    instrument = models.CharField(max_length=100, verbose_name="Camera Name")
    aperture = models.FloatField(verbose_name="Telescope Aperture (mm)")
    telescope = models.CharField(max_length=100, verbose_name="Telescope Type")