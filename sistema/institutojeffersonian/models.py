from django.db import models


# Create your models here.
class Beneficiario(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre', null=True)
    rfc = models.CharField(max_length=13, verbose_name='RFC', null=True)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "RFC: " + self.rfc
        return fila
