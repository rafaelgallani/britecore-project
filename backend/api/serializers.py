from .models import RiskType, Field, FieldValue, Risk, RiskField, RiskTypeDefaultField
from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin

class DefaultSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class RiskTypeDefaultFieldChildSerializer(DefaultSerializer):
    class Meta(DefaultSerializer.Meta):
        model = RiskTypeDefaultField
        
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

class RiskTypeFieldSerializer(DefaultSerializer):
    name = serializers.CharField()
    field_type = serializers.CharField()

    class Meta(DefaultSerializer.Meta):
        model = RiskTypeDefaultField
        fields = ['field_type', 'name']
        
class RiskTypeSerializer(DefaultSerializer):
    
    fields = RiskTypeFieldSerializer(many=True)

    class Meta(DefaultSerializer.Meta):
        model = RiskType

    def create(self, validated_data):
        fields = validated_data.pop('fields')
        risk_type = RiskType.objects.create(**validated_data)
        
        for field in fields:
            default_field = RiskTypeDefaultField.objects.create(
                field = Field.objects.create(**field),
                risk_type = risk_type
            )
        return risk_type