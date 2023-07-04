from rest_framework import serializers
from .models import Book

from copies.models import Copy


class BookSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Book:
        book = Book.objects.create(**validated_data)

        number_copies = book.num_copies

        while number_copies > 0:
            Copy.objects.create(book=book)
            number_copies -= 1

        return book

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "book_genre",
            "synopsis",
            "publishing_company",
            "num_copies",
        ]
