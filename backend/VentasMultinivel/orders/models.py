from django.db import models
from regions.models import region
from users.models import cliente
from warehouse.models import producto

# Create your models here.
class metodopago(models.Model):
    k_metodo = models.CharField(max_length=2, primary_key=True)
    t_descripcion = models.CharField(max_length=20)

class pedido(models.Model):
    k_pedido = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    f_creacion = models.DateField()
    i_estado = models.CharField(max_length=1)
    n_direccion = models.CharField(max_length=50)
    k_region = models.ForeignKey(region, on_delete=models.CASCADE)
    k_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)

class pedi_item(models.Model):
    k_pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    k_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    n_cantidad = models.DecimalField(max_digits=5, decimal_places=0)
    n_preciou = models.DecimalField(max_digits=6, decimal_places=0)

class caliservicio(models.Model):
    k_pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    n_calificacion = models.DecimalField(max_digits=1, decimal_places=0)

class pagopedido(models.Model):
    k_pagopedido = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    n_valor = models.DecimalField(max_digits=10, decimal_places=0)
    i_estado = models.CharField(max_length=1)
    f_pago = models.DateField()
    k_pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    k_metodo = models.ForeignKey(metodopago, on_delete=models.CASCADE)

