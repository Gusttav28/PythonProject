from rest_framework import serializers
from .models import Users, DynamicSchema, DynamicItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
                        
class DynamicSchemaSerializer(serializers.ModelSerializer):
    # def validate_schema(self, value):
    #     allowed_types = {"string", "numbers"}
    #     fields = value.get("fields", {})

    #     if not fields:
    #         raise serializers.ValidationError("The schema (table) must have at least one field")
        
    #     for field_name, field_type in field.items():
    #         if field_type not in allowed_types:
    #             raise serializers.ValidationError(
    #                 f"Invalid type '{field_type}' for field '{field_name}.'"
    #             )
        
    #     return value
            
            
    class Meta:
        model = DynamicSchema
        fields = "__all__"
  
class DynamicItemSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        def validate(self, attrs):
            if not attrs:
                raise serializers.ValidationError(
                    "No valid fields provided for this schema."
                )
            return attrs
        
        schema_instance = self.context.get('schema_instance')
        if schema_instance:
            for field_name, field_type in schema_instance['fields'].items():
                if field_type == 'string':
                    self.fields[field_name] = serializers.CharField()
                elif field_type == 'number':
                    self.fields[field_name] = serializers.IntegerField()
                    
    def create(self, validated_data):
        schema = self.context['schema_model']
        return DynamicItem.objects.create(
            schema_def = schema,
            data = validated_data
        )
        
    def to_representation(self, instance):
        return instance.data  