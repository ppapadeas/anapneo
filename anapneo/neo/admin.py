from django.contrib import admin
from anapneo.neo.models import Neo

class NeoAdmin(admin.ModelAdmin):
    list_display = ['user', 'observation_date', 'position_ra', 'position_dec', 
                    'magnitude', 'exposure', 'instrument', 'aperture', 'telescope']
    
admin.site.register(Neo, NeoAdmin)
