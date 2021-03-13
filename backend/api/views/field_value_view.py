from rest_framework import viewsets
from ..models import FieldValue
from ..serializers import FieldValueSerializer

class FieldValueViewSet(viewsets.ModelViewSet):
    queryset = FieldValue.objects.all()
    serializer_class = FieldValueSerializer

