from django.test import TestCase

# Create your tests here.
from ..models import Risk, Field, RiskField

from .test_risk import valid_record as valid_risk
from .test_field import valid_record as valid_field


def valid_record():
    return {
        "risk": Risk.objects.create(**valid_risk()), 
        "field": Field.objects.create(**valid_field()), 
    }

class RiskFieldUnitTest(TestCase):
    def setUp(self):
        RiskField.objects.create(**valid_record())

    def test_risk_field_has_all_attributes(self):
        expected_risk_field = valid_record()
        
        risk_field = RiskField.objects.all()[0]
        
        self.assertEqual(type(risk_field.field), Field)
        self.assertEqual(type(risk_field.risk), Risk)

        self.assertEqual(risk_field.field.name, (expected_risk_field['field'].name)) 
        self.assertEqual(risk_field.risk.name, (expected_risk_field['risk'].name)) 
