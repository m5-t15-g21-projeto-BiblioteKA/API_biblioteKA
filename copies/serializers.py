from rest_framework import serializers
from .models import Copy

from books.seriliazers import BookSerializer


class CopySerialzer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Copy
        fields = [
            "id",
            "available",
            "book",
        ]
