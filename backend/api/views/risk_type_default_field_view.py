from rest_framework import viewsets
from ..models import RiskTypeDefaultField
#from ..serializers import RiskTypeDefaultFieldSerializer

class RiskTypeDefaultFieldViewSet(viewsets.ModelViewSet):
    queryset = RiskTypeDefaultField.objects.all()
    #serializer_class = RiskTypeDefaultFieldSerializer

