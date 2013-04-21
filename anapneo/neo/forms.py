from django.forms import ModelForm
from anapneo.neo.models import Neo

class NeoForm(ModelForm):
    class Meta:
        model = Neo
    
