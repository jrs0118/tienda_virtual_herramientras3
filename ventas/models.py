from django.db import models
from inventario.models import Productos

class Venta(models.Model):
    id_venta = models.AutoField(primary_key = True)
    nombres = models.TextField(max_length=30)
    tipo_doc = models.CharField(max_length=30)
    num_doc = models.IntegerField(default=0)
    correo = models.EmailField()
    direccion = models.CharField(max_length=30)
    depto = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    telefono = models.IntegerField(default=0)
    total_venta = models.DecimalField(max_digits=50,decimal_places=3,null =False) 