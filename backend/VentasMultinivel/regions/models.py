from django.db import models
import json

# Create your models here.
class pais(models.Model):
    k_pais = models.CharField(max_length=2, primary_key=True)
    t_nombre = models.CharField(max_length=30, unique=True)

class region(models.Model):
    k_region = models.CharField(max_length=3, primary_key=True)
    k_pais = models.ForeignKey(pais, on_delete=models.RESTRICT)
    t_nombre = models.CharField(max_length=30, unique=True)
    class Meta:
        unique_together = (('k_region','k_pais'),)
def add_pais(cod,nombre):
    try:
        pais.objects.create(k_pais=cod,t_nombre=nombre)
        return "Se agregó el pais '%s'" % nombre
    except:
        return "Ya existe un pais con el nombre '%s'" % nombre
    
def get_paises():
    paises = list(pais.objects.all().values())
    file = open('VentasMultinivel/Templates/Countries.json', 'r').read()
    data = json.dumps(paises)
    if file != data:
        open('VentasMultinivel/Templates/Countries.json', 'w').write(data)