from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only = True)
    # we put a slug related field in order to overwrite that field
    author_name = serializers.SlugRelatedField(
        # so we need to check for the information that we wanna overwrite by taking the field from the model in where the field came from 
        queryset = Author.objects.all(),
        slug_field = "name",
    )
    
    class Meta:
        model = Book
        fields = "__all__"

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = loan
        fields = "__all__"
        
    def validate(self, initial_data):
        return initial_data
