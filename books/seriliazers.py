from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "book_genre",
            "synopsis",
            "publishing_company",
            "num_copies"
        ]
