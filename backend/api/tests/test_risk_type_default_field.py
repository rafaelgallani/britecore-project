from django.test import TestCase

# Create your tests here.
from ..models import RiskType, Field, RiskTypeDefaultField
from .test_risk_type import valid_record as valid_risk_type
from .test_field import valid_record as valid_field


def valid_record():
    return {
        "risk_type": RiskType.objects.create(**valid_risk_type()), 
        "field": Field.objects.create(**valid_field()), 
    }

class RiskTypeDefaultFieldUnitTest(TestCase):
    def setUp(self):
        RiskTypeDefaultField.objects.create(**valid_record())

    def test_risk_type_default_field_has_all_attributes(self):
        expected_risk_type_default_field = valid_record()
        
        risk_type_default_field = RiskTypeDefaultField.objects.all()[0]
        
        self.assertEqual(type(risk_type_default_field.field), Field)
        self.assertEqual(type(risk_type_default_field.risk_type), RiskType)

        self.assertEqual(risk_type_default_field.field.name, (expected_risk_type_default_field['field'].name)) 
        self.assertEqual(risk_type_default_field.risk_type.name, (expected_risk_type_default_field['risk_type'].name)) 
