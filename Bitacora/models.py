from operator import truediv
from pyexpat import model
from statistics import mode
from django.db import models

class BitacoraModel(models.Model):
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    contador = models.IntegerField(default=0)
    trabajos = models.TextField()
    tecnico = models.CharField(max_length=100)
    finalizado = models.DateField(auto_now_add=True)

# Create your models here.
