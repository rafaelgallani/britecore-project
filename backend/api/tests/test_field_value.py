from django.test import TestCase

# Create your tests here.
from ..models import Field, FieldValue
from .test_field import valid_record as valid_field

def valid_record():
    return {
        "label": "New field value", 
        "value": "Test", 
        "field": Field.objects.create(**valid_field())
    }

class FieldValueUnitTest(TestCase):
    def setUp(self):
        FieldValue.objects.create(**valid_record())

    def test_field_value_has_all_attributes(self):
        expected_field_value = valid_record()

        field_value = FieldValue.objects.all()[0]
        
        self.assertEqual(field_value.label, expected_field_value["label"])
        self.assertEqual(field_value.value, expected_field_value["value"])
        
        self.assertEqual(field_value.field.name, expected_field_value["field"].name)
