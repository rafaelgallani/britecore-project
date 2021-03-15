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

class RiskFieldSerializer(DefaultSerializer):
    field = FieldSerializer()
    risk = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    value = serializers.CharField()

    class Meta(DefaultSerializer.Meta):
        model = RiskField
        depth = 0

class RiskSerializer(DefaultSerializer):
    fields = RiskFieldSerializer(many=True)

    class Meta(DefaultSerializer.Meta):
        model = Risk

    def create(self, validated_data):
        fields = validated_data.pop('fields')
        risk = Risk.objects.create(**validated_data)
        all_fields = []

        for field in fields:
            
            risk_field_value = field.pop('value')

            field_data = field.pop('field')
            field_options = field_data.pop('options', []);

            created_field = Field.objects.create(**field_data)
            
            options = []

            for option in field_options:
                created_option = FieldValue.objects.create(
                    **option,
                    field=created_field
                )
                options.append(created_option)
            
            created_field.options.set(options)

            default_field = RiskField.objects.create(
                value = risk_field_value,
                field = created_field,
                risk = risk
            )
            all_fields.append(default_field)
        
        risk.fields.set(all_fields)

        return risk


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
    
    risks = RiskSerializer(many=True, required=False)
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