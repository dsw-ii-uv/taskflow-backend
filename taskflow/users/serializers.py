from django.conf import settings
from django.contrib.auth.models import Group
from rest_framework import serializers
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from users.models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    """Serializer for user sign-up."""
    class Meta:
        model = User
        exclude = [
            "is_active",
        ]


class UserSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "birth_date",
            "identification_type",
            "identification_number",
            "gender",
            "phone_number",
            "address",
            "email",
            "group",
        ]


class LogoutSerializer(serializers.Serializer):
    pass
