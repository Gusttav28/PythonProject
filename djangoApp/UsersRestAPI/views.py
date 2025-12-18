from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import action
import requests
from rest_framework import status
# Create your views here


class OcupationViewSerializer(viewsets.ModelViewSet):
    queryset = UsersOcupation.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserOcupationSerializer
        
        
class DynamicTableViewSerializer(viewsets.ModelViewSet):
    queryset = DynamicTableForOcupations.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class = DynamicTableSerializer
    

class DynamicItemViewSerializer(viewsets.ModelViewSet):
    queryset = DynamicItemFortheTable.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DynamicItemSerializer