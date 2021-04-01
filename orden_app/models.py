from django.db import models

from django.urls import reverse

class Proceso(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Orden(models.Model):
    nombre = models.CharField(max_length=100)
    proceso = models.ManyToManyField(Proceso, through='Ordenes_procesos')
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('orden_app:index')

class Ordenes_procesos(models.Model):
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    nota = models.CharField(max_length=100)
    fecha = models.DateTimeField()
