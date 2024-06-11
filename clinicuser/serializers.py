from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "full_name", "address", "phone", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError(
                "Password must be at least 6 characters long."
            )
        return value

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            full_name=validated_data.get("full_name"),
            phone=validated_data.get("phone"),
            address=validated_data.get("address"),
            username = validated_data.get("email")
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)