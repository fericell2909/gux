from rest_framework import viewsets
from .models import Testings
from .serializers import TestingsSerializers
from django_filters.rest_framework import DjangoFilterBackend, filters
from .filters import Testingsfilter

from rest_framework.filters import SearchFilter, OrderingFilter

class TestingsViewSet(viewsets.ModelViewSet):
    filter_class = Testingsfilter
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    queryset = Testings.objects.all().order_by('-id')
    serializer_class = TestingsSerializers
