from django.forms import ModelForm
from anapneo.neo.models import Neo, UserProfile


class NeoForm(ModelForm):
    class Meta:
        model = Neo
        exclude = ('user',)


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'email')
