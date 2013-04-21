from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(max_length=100)
    display_name = models.CharField(max_length=50, unique=True,
        validators=[
            RegexValidator(regex=r'("")|(^[a-z0-9_]+$)',
                           message='Please only a-z characters, numbers and '
                                   'underscores.')])
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


class Observation(models.Model):
    user = models.ForeignKey(User)
    observation_date = models.DateTimeField(verbose_name="Observation Date")
    position_ra = models.CharField(max_length=100, verbose_name="R.A.")
    position_dec = models.CharField(max_length=100, verbose_name="Declination")
    magnitude = models.CharField(max_length=100, verbose_name="Magnitude")
    exposure = models.FloatField(verbose_name="Exposure Time (sec)")
    instrument = models.CharField(max_length=100, verbose_name="Camera Name")
    aperture = models.FloatField(verbose_name="Telescope Aperture (mm)")
    telescope = models.CharField(max_length=100, verbose_name="Telescope Type")


class Neo(models.Model):
    obsrv_range = models.ManyToManyField(Observation)
    mean_date = models.DateTimeField(verbose_name="Mean Observation Date")
    mean_ra = models.CharField(max_length=100, verbose_name="Mean R.A.")
    mean_dec = models.CharField(max_length=100, verbose_name="Mean Declination")
