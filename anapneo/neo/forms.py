from django.forms import Form, ModelForm, ChoiceField, RadioSelect
from anapneo.neo.models import Neo, UserProfile, Feedback


CHOICES = [(1, 'Upvote'), (-1, 'Downvote')]


class NeoForm(ModelForm):
    class Meta:
        model = Neo
        exclude = ('user',)


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'email')


class FeedbackForm(Form):
    vote = ChoiceField(choices=CHOICES, widget=RadioSelect())
