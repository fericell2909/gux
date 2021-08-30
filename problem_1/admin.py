from django.contrib import admin
from gux.admin import AuditAdmin
# Register your models here.
from .models import Testings

@admin.register(Testings)
class TestingsAdmin(AuditAdmin):
    search_fields=("numero_rol", "nombre_paciente", "fecha_prevision", "fecha_alta")
    list_display = ('id', 
                "numero_rol",
                "nombre_paciente",
                "fecha_hospitalizacion",
                "fecha_alta",
                "fecha_prevision",
                "codigo_prevision",
                "accion",
                "numero",
                "tipo_RAM")

    

