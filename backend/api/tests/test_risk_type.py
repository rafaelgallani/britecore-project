from django.test import TestCase

# Create your tests here.
from ..models import RiskType

def valid_record():
    return {
        "name": "New Risk Type", 
        "description": "New Risk Type description",
    }

class RiskTypeUnitTest(TestCase):
    def setUp(self):
        RiskType.objects.create(**valid_record())

    def test_risk_type_has_all_attributes(self):
        risk_type = RiskType.objects.get(name="New Risk Type")
        
        self.assertEqual(risk_type.name, "New Risk Type")
        self.assertEqual(risk_type.description, "New Risk Type description")
