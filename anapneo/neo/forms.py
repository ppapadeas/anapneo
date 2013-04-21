from django.forms import ModelForm
from anapneo.neo.models import Neo, UserProfile, Feedback


class NeoForm(ModelForm):
    class Meta:
        model = Neo
        exclude = ('user', 'no', 'created')


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'email')


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ('user', 'neo')
