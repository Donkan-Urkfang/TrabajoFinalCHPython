from django.contrib import admin

from Entregable.models import Juego, Desarrolladora, Profile, Avatar

# Register your models here.

admin.site.register(Juego)
admin.site.register(Desarrolladora)
admin.site.register(Avatar)   
admin.site.register(Profile)