from rest_framework import serializers
from .models import *


class UserOcupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersOcupation
        fields = "__all__"
        
    

class DynamicTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicTableForOcupations
        fields = "name"
        
class DynamicItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicItemFortheTable
        fields = "__all__"