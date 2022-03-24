from django.contrib import admin
from .models import Servicio #el .models nos indica que models esta en el mismo directorio
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    #vamos a agregar los campos created y updates especificando que son de solo lecura
    readonly_fields=('created','updated')
admin.site.register(Servicio,ServicioAdmin) #registramos el modelo servicio

