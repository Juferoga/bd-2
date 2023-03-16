from django.db import models
from regions.models import region
# Create your models here.

class bodega(models.Model):
    k_bodega = models.DecimalField(max_digits=6, decimal_places=0, primary_key=True)
    t_direrccion = models.CharField(max_length=50)
    n_telefono = models.DecimalField(max_digits=10, decimal_places=0)
    k_region = models.ForeignKey(region, on_delete=models.CASCADE)

class categoria(models.Model):
    k_categoria = models.CharField(max_length=3, primary_key=True)
    t_descripcion = models.CharField(max_length=30)
    k_superior = models.ForeignKey('self', on_delete=models.CASCADE)
    
class producto(models.Model):
    k_producto = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    t_nombre = models.CharField(max_length=30)
    t_descripcion = models.CharField(max_length=100)
    k_categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)

class bode_prod(models.Model):
    k_bodega = models.ForeignKey(bodega, on_delete=models.CASCADE)
    k_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    n_cantidad = models.DecimalField(max_digits=8, decimal_places=0)
    class Meta:
        unique_together = (('k_bodega','k_producto'),)