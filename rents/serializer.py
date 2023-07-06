from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from django.core.exceptions import ObjectDoesNotExist
from .models import Rent
from users.serializers import UserSerializer
from copies.serializers import CopySerialzer
from books.seriliazers import BookSerializer
from copies.models import Copy
from users.models import User
from users.serializers import UserStatusSerializer
from datetime import datetime, timedelta


class RentSerializer(serializers.ModelSerializer):
    book = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    copy = CopySerialzer(read_only=True)

    def create(self, validated_data):
        user_id = validated_data.pop("user_id", None)
        book_id = validated_data.pop("book", None)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError({"msg": "Invalid user ID"})

        copy = Copy.objects.filter(book_id=book_id, available=True).first()
        if user.can_locate:
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
        else:
            raise ValidationError({"msg": "User can't locate a book"})

    class Meta:
        model = Rent
        fields = [
            "id",
            "date_rent",
            "date_limit",
            "date_devolution",
            "user",
            "user_id",
            "copy",
            "book",
        ]


class RentDevolutionSerializer(serializers.ModelSerializer):
    user = UserStatusSerializer()
    copy = CopySerialzer()

    def update(self, instance: Rent, validated_data):
        if instance.date_devolution:
            raise ValidationError({"msg": "Copy already returned"})
        current_date = datetime.now().date()
        instance.date_devolution = current_date
        instance.save()

        print(instance.date_devolution > instance.date_limit)

        if instance.date_devolution > instance.date_limit:
            instance.user.can_locate = False
            instance.user.save()

        instance.copy.available = True
        instance.copy.save()

        return instance

    class Meta:
        model = Rent
        fields = [
            "id",
            "date_rent",
            "date_limit",
            "date_devolution",
            "user",
            "copy",
        ]
