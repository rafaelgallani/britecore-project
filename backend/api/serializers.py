from .models import RiskType, Field, FieldValue, Risk, RiskField, RiskTypeDefaultField
from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin

class DefaultSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class RiskTypeDefaultFieldChildSerializer(DefaultSerializer):
    class Meta(DefaultSerializer.Meta):
        model = RiskTypeDefaultField
        
class FieldValueSerializer(DefaultSerializer):
    class Meta(DefaultSerializer.Meta):
        model = FieldValue
        fields = None
        exclude = ['field']

class FieldSerializer(DefaultSerializer):
    options = FieldValueSerializer(many=True, required=False)
    class Meta(DefaultSerializer.Meta):
        model = Field
    
    def create(self, validated_data):
        options = validated_data.pop('options')
        field = Field.objects.create(**validated_data)
        
        for option in options:
            created_option = FieldValue.objects.create(
                **option,
                field=field
            )

        return field
        
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
    options = FieldValueSerializer(many=True, required=False)

    class Meta(DefaultSerializer.Meta):
        model = RiskTypeDefaultField
        fields = ['field_type', 'name', 'options']
        
class RiskTypeSerializer(DefaultSerializer):
    
    fields = RiskTypeFieldSerializer(many=True)

    class Meta(DefaultSerializer.Meta):
        model = RiskType

    def create(self, validated_data):
        fields = validated_data.pop('fields')
        risk_type = RiskType.objects.create(**validated_data)
        
        for field in fields:
            
            field_options = field.pop('options', []);
            created_field = Field.objects.create(**field)
            
            options = []

            for option in field_options:
                created_option = FieldValue.objects.create(
                    **option,
                    field=created_field
                )
                options.append(created_option)
            
            created_field.options.set(options)

            default_field = RiskTypeDefaultField.objects.create(
                field = created_field,
                risk_type = risk_type
            )

        return risk_type