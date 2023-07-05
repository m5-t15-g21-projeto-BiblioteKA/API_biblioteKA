from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from django.core.exceptions import ObjectDoesNotExist
from .models import Rent
from users.serializers import UserSerializer
from copies.serializers import CopySerialzer
from books.seriliazers import BookSerializer
from copies.models import Copy
from users.models import User
from datetime import datetime, timedelta


class RentSerializer(serializers.ModelSerializer):
    book = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    book_details = BookSerializer(source='copy.book', read_only=True)

    def create(self, validated_data):
        user_id = validated_data.pop("user_id", None)
        book_id = validated_data.pop("book", None)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError({"msg": "Invalid user ID"})

        copy = Copy.objects.filter(book_id=book_id, available=True).first()

        if copy:
            validated_data["copy"] = copy
            copy.available = False
            copy.save()
        else:
            raise ValidationError({"msg": "Copy unavailable"})

        date_rent = validated_data.get("date_rent", datetime.now().date())
        date_limit = date_rent + timedelta(days=15)
        # checar se nao está caindo no final de semana
        if date_limit.weekday() >= 5:
            days_to_add = 7 - date_limit.weekday()
            date_limit += timedelta(days=days_to_add)

        validated_data["date_limit"] = date_limit
        validated_data["user"] = user
        validated_data["user_id"] = user.id

        return Rent.objects.create(**validated_data)

    class Meta:
        model = Rent
        fields = ["id", "date_rent", "date_limit",
                  "date_devolution", "user", "user_id", "book", "book_details"]
