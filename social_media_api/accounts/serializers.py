from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password2 = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = '__all__'
        
    def create(self, validated_data):
        validated_data.pop("password")
        return User.objects.create_user(   # <-- THIS IS get_user_model().objects.create_user()
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],)

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()