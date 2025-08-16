from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.decorators import action
from .models import Users
from .serializers import UserSerializer
import requests


# Create your views here.
class UserViewSets(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    
    
    @action(detail=False, methods=['GET'])
    def get_users(self, request):
        user = self.get_object()
        return Response({
            'status': 'successfully'
        }, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def add_users(self, request, pk=None):
        user = self.get_object(pk=pk)
        user.status = "created"
        user.save()
        print(user)
        return Response({
            'status':'user created successfully'
        }, status= status.HTTP_201_CREATED)
        
    # @action(detail=True, methods=['PUT'])
    # def add_users(self, request, pk=None):
    #     user = self.get_object(pk=pk)
    #     user.status = "updated"
    #     user.save()
    #     return Response({
    #         'status':'user updated successfully'
    #     }, status= status.HTTP_201_CREATED)

    
def index(request):
    return render(request, 'index.html')