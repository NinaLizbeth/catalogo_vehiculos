from django.contrib import admin
from .models import Vehiculo

# Register your models here.

admin.site.register(Vehiculo)

#class vehiculosAdmin(admin.ModelAdmin):
    #readonly_fields = ('fecha_creacion', 'fecha_modificacion')
   # list_display = ('modelo')
