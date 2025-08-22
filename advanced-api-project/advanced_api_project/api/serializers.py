from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Adds validation to ensure publication_year is not in the future.
    """

    class Meta :
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication yeare cannot be in the future.")
        return value

class Autoserializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes nested serialization of the related Book instances.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']