from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.decorators import action
from .models import Users
from .serializers import UserSerializer
import requests
from django.shortcuts import get_object_or_404
from .models import DynamicSchema, DynamicItem
from .serializers import DynamicSchemaSerializer, DynamicItemSerializer

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



class DynamicSchemaView(APIView):
    def get(self, request):
        schemas = DynamicSchema.objects.all()
        serializer = DynamicSchemaSerializer(schemas, many = (True))
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DynamicSchemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                


class DynamicItemView(APIView):
    def get(self, request, schema_id):
        schema = get_object_or_404(DynamicSchema, id=schema_id)
        items = DynamicItem.objects.filter(schema_def=schema)
        
        serializer = DynamicItemSerializer(
            items, 
            many=True,
            context = {
                "schema_instance": schema.schema,
                "schema_model": schema,
            }
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, schema_id):
        schema = get_object_or_404(DynamicSchema, id=schema_id)
        
        serializer = DynamicItemSerializer(
            data = request.data,
            context = {
                "schema_instance": schema.schema,
                "schema_model": schema,
                
            }
        )
        
        if serializer.is_valid():
            item = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)