from rest_framework import viewsets, permissions
from rest_framework.response import Response
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

class LoanViewSerializer(viewsets.ModelViewSet):
    queryset = loan.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanSerializer 