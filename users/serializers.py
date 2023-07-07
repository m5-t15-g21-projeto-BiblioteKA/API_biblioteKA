from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "username",
            "password",
            "is_colaborator",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with this email already exists.",
                    )
                ]
            },
        }

    def validate(self, attrs):
        is_colaborator = attrs.get("is_colaborator", False)
        if is_colaborator:
            attrs["is_superuser"] = True
            attrs["is_staff"] = True

        return super().validate(attrs)

    def create(self, validated_data: dict):
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                value = make_password(value)
            setattr(instance, key, value)

        instance.save()

        return instance


class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "email",
            "is_colaborator",
            "can_locate",
        ]
