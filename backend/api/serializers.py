from .models import RiskType, Field, FieldValue, Risk, RiskField, RiskTypeDefaultField
from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin

class DefaultSerializer(QueryFieldsMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'

class RiskTypeSerializer(DefaultSerializer):
    class Meta(DefaultSerializer.Meta):
        model = RiskType
        
class FieldSerializer(DefaultSerializer):
    class Meta(DefaultSerializer.Meta):
        model = Field
        
class FieldValueSerializer(DefaultSerializer):
    class Meta(DefaultSerializer.Meta):
        model = FieldValue
        
class RiskSerializer(DefaultSerializer):
    class Meta(DefaultSerializer.Meta):
        model = Risk
        
class RiskFieldSerializer(DefaultSerializer):
    class Meta(DefaultSerializer.Meta):
        model = RiskField
        
class RiskTypeDefaultFieldSerializer(DefaultSerializer):
    class Meta(DefaultSerializer.Meta):
        model = RiskTypeDefaultField
        