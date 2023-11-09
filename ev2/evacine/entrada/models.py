from django.db import models

class EntradaCine(models.Model):
    Codigo_de_entrada = models.CharField(max_length=255)
    Hora = models.DateTimeField()
    Fecha = models.DateField()
    butaca = models.CharField(max_length=255)
    sala = models.CharField(max_length=255)
    nombre_cine = models.CharField(max_length=255)

    def __str__(self):
        return self.Codigo_de_entrada
