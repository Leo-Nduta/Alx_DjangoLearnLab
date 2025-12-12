from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required = True, write_only = True)
    password2 = serializers.CharField(required = True, write_only = True)
    
    class Meta:
        model = CustomUser
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 25)
    password = serializers.CharField(write_only = True)