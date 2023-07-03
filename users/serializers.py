from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


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
        if self.instance is None and attrs["is_colaborator"] is True:
            attrs["is_superuser"] = True

        return super().validate(attrs)

    def create(self, validated_data: dict):
        return User.objects.create_user(**validated_data)
