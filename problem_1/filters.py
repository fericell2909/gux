from django_filters import FilterSet
from .models import Testings


class Testingsfilter(FilterSet):
    """
    Testings Filter
    """
    class Meta: 
        model = Testings
        fields = {
            'numero_rol': ['contains', 'exact'],
            'nombre_paciente': ['contains', 'exact'],
            'fecha_hospitalizacion': ['contains', 'exact'],
            'fecha_alta': ['contains', 'exact'],
            'codigo_prevision': ['contains', 'exact']
        }