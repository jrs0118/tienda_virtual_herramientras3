from django.db import models

# Create your models here.
class Productos(models.Model):
    id_producto = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    cost = models.IntegerField(default=0)
    cantidad_stock = models.IntegerField(default=0)
    description = models.TextField(max_length=30)
    imagen = models.ImageField(upload_to='media/', null=True)
