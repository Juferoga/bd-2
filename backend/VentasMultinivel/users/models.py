from django.db import models
from regions.models import region

# Create your models here.
class clasificacion(models.Model):
    k_clasificacion = models.CharField(max_length=3, primary_key=True)
    t_descripcion = models.CharField(max_length=15)
    n_comision = models.DecimalField(max_digits=4, decimal_places=3)

class usuario(models.Model):
    k_usuario = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    t_email = models.CharField(max_length=50)
    t_password = models.CharField(max_length=60)

class representante(models.Model):
    k_representante = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    t_nombre = models.CharField(max_length=30)
    t_apellido = models.CharField(max_length=30)
    f_nacimiento = models.DateField()
    i_genero = models.CharField(max_length=1)
    n_telefono = models.DecimalField(max_digits=10, decimal_places=0)
    f_contrato = models.DateField()
    t_direccion = models.CharField(max_length=50)
    k_region = models.ForeignKey(region, on_delete=models.RESTRICT, null=True)
    k_clasificacion = models.ForeignKey(clasificacion, on_delete=models.RESTRICT, null=True)
    k_usuario = models.ForeignKey(usuario, on_delete=models.RESTRICT, null=True)
    k_jefe = models.ForeignKey('self', on_delete=models.RESTRICT, null=True)

class cliente(models.Model):
    k_cliente = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    t_nombre = models.CharField(max_length=30)
    t_apellido = models.CharField(max_length=30)
    n_telefono = models.DecimalField(max_digits=10, decimal_places=0)
    k_representante = models.ForeignKey(representante, on_delete=models.RESTRICT, null=True)
    k_usuario = models.ForeignKey(usuario, on_delete=models.RESTRICT, null=True)
