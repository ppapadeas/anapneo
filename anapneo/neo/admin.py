from django.contrib import admin
from anapneo.neo.models import Neo, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'first_name', 'last_name', 'city', 
                    'country', 'lat', 'lon']

admin.site.register(UserProfile, UserProfileAdmin)

class NeoAdmin(admin.ModelAdmin):
    list_display = ['user', 'score', 'observation_date', 'position_ra', 
                    'position_dec', 'magnitude', 'updated', 'note', 'num_obs', 
                    'arc', 'nominal_h']
        
admin.site.register(Neo, NeoAdmin)
