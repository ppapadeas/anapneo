from django.contrib import admin
from anapneo.neo.models import Observation, Neo, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'first_name', 'last_name', 'city', 
                    'country', 'lat', 'lon']

admin.site.register(UserProfile, UserProfileAdmin)

class ObservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'observation_date', 'position_ra', 'position_dec', 
                    'magnitude', 'exposure', 'instrument', 'aperture', 'telescope']
    
admin.site.register(Observation, ObservationAdmin)


class NeoAdmin(admin.ModelAdmin):
    list_display = ['mean_date', 'mean_ra', 'mean_dec']
    
admin.site.register(Neo, NeoAdmin)
