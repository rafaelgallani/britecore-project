from django.test import TestCase

# Create your tests here.
from ..models import Risk, RiskType
from .test_risk_type import valid_record as valid_risk_type

def valid_record():
    return {
        "name": "New Risk", 
        "description": "New Risk",
        "risk_type": RiskType.objects.create(**valid_risk_type())
    }

class RiskUnitTest(TestCase):
    def setUp(self):
        Risk.objects.create(**valid_record())

    def test_risk_has_all_attributes(self):
        expected_risk, expected_risk_type = valid_record(), valid_risk_type()

        risk = Risk.objects.get(name=expected_risk["name"])
        
        self.assertEqual(risk.name, expected_risk["name"])
        self.assertEqual(risk.description, expected_risk["description"])
        self.assertEqual(type(risk.risk_type), RiskType)
        
        self.assertEqual(risk.risk_type.name, expected_risk_type["name"])
