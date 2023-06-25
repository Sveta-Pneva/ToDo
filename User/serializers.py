from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "firstname",
            "surname",
            "email",
        )

class CustomUserFullModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "firstname",
            "surname",
            "email",
            "is_superuser",
            "is_staff",
        )