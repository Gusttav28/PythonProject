from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import UsersOcupation
from .serializers import UserOcupationSerializer
from rest_framework.decorators import action
import requests
from rest_framework import status
# Create your views here


class OcupationViewSerializer(viewsets.ModelViewSet):
    queryset = UsersOcupation.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserOcupationSerializer
        