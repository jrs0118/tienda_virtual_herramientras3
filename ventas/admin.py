from django.contrib import admin
from ventas.models import Venta

# Register your models here.
class VentaAdmin(admin.ModelAdmin):
    list_display=('name', 'identificacion', 'correo', 'direccion', 'telefono')
    search_fields = ('name', 'identificacion')

admin.site.register(Venta)
