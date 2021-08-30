from django.db import models
from django.db.models.fields import DateField
from django.db.models.fields.related import ForeignKey
from gux.models import AuditModel

"""
    I have created the name of the fields in Spanish following the instructions in the image.
    He creado el nombre de los campos en español siguiendo las instrucciones de la imagen.
"""

class Testings(AuditModel):

    numero_rol = models.IntegerField("Numero de rol", )
    nombre_paciente = models.CharField("Nombre del paciente", max_length=50)
    fecha_hospitalizacion = models.DateField("Fecha de hospitalizacion")
    fecha_alta = models.DateField("Fecha de alta")
    fecha_prevision = models.DateField("Fecha de previsión", null=True, blank=True)
    codigo_prevision = models.CharField("Codigo de previson", max_length=50)
    accion = models.CharField("Accion", max_length=50)
    numero = models.IntegerField("Numero",)
    tipo_RAM = models.CharField("tirpo_RAM", max_length=50, null=True, blank=True)

    def __int__ (self):
        return self.id


"""
    Luego de analizar la imagen no logre detectar relaciones con ninguna otra 
    tabla, por esa razón ninguno de los campos es de tipo ForeignKey. 
"""