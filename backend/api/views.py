from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import RiskTypeSerializer
from .models import RiskType


class TestViewSet(viewsets.ModelViewSet):
    queryset = RiskType.objects.all().order_by('name')
    serializer_class = RiskTypeSerializer
