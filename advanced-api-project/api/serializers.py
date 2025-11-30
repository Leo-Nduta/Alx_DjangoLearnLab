from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

#The BookSerializer is used to enable easy access to books for retrieval
class BookSerializer(serializers.ModelSerializer):
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value < current_year:
            raise serializers.ValidationError("Publication cannot be in the future.")
        return value
    
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']