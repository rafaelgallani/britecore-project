from django.test import TestCase

# Create your tests here.
from ..models import Field

def valid_record():
    return {
        "name": "Test field",
        "field_type": Field.FieldType.TEXT
    }

class FieldUnitTest(TestCase):
    def setUp(self):
        Field.objects.create(**valid_record())

    def test_risk_has_all_attributes(self):
        expected_field = valid_record()

        field = Field.objects.get(name=expected_field["name"])
        
        self.assertEqual(field.name, expected_field["name"])
        self.assertEqual(field.field_type, expected_field["field_type"])