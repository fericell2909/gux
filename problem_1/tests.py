from django.test import TestCase
from .models import Testings

class TestingsTestCase(TestCase):
    def setUp(self):
        Testings.objects.create(
            numero_rol = 12345678,
            nombre_paciente = "Ruben Carvajal",
            codigo_prevision = "QWASEDRFTG",
            accion = "CL",
            numero = "1",
            tipo_RAM = ""
        )


    def test_testing(self):
        numero_rol = Testings.objects.get(numero_rol=12345678)
        nombre_paciente = Testings.objects.get(nombre_paciente="Ruben Carvajal")
        codigo_prevision = Testings.objects.get(codigo_prevision="QWASEDRFTG")
        accion = Testings.objects.get(accion="CL")
        numero = Testings.objects.get(numero="1")
        tipo_RAM = Testings.objects.get(tipo_RAM="")
