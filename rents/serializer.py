from rest_framework import serializers
from .models import Rent
from users.serializers import UserSerializer
from copies.serializers import CopySerialzer

from copies.models import Copy


class RentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # se daqui as 30 cair em um final de semana mudar a data de devolução
        # copy_test = Copy.objects.get(id=1)

        return Rent.objects.create(**validated_data, copy_id=1, user_id=1)

    user = UserSerializer(read_only=True)
    copy = CopySerialzer(read_only=True)

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
