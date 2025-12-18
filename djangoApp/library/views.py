from rest_framework import viewsets, permissions, generics
from rest_framework.filters import SearchFilter
from .models import *
from .serializers import *
from rest_framework.decorators import action
import requests
from rest_framework import status

# Create your views here.

class AuthorViewSerializer(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorSerializer 

class BookViewSerializer(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BookSerializer
    
class MemberViewSerializer(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MemberSerializer 
    filter_backends = [SearchFilter]
    search_fields = ['cx_name']


class LoanViewSerializer(viewsets.ModelViewSet):
    queryset = loan.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','phoneNumber'] 