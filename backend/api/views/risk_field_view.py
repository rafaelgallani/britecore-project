from rest_framework import viewsets
from ..models import RiskField
from ..serializers import RiskFieldSerializer

class RiskFieldViewSet(viewsets.ModelViewSet):
    queryset = RiskField.objects.all()
    serializer_class = RiskFieldSerializer

