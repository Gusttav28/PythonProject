from rest_framework import serializers
from .models import UsersOcupation


class UserOcupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersOcupation
        fields = "__all__"