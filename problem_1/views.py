from rest_framework import viewsets
from .models import Testings
from .serializers import TestingsSerializers
from django_filters.rest_framework import DjangoFilterBackend, filters
from .filters import Testingsfilter
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.filters import SearchFilter, OrderingFilter

class TestingsViewSet(viewsets.ModelViewSet):
    filter_class = Testingsfilter
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    queryset = Testings.objects.all().order_by('-id')
    serializer_class = TestingsSerializers

    @action(detail=False, methods=['GET'])
    def all_pevesion(self, request):
        queryset = Testings.objects.all()  
        list_all_prevision = []
        for i in  queryset:
            list_all_prevision.append(i.codigo_prevision)

        return Response ({"result": list_all_prevision})
