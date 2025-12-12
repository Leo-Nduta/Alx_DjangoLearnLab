from django.shortcuts import render
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import CustomUser

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user_id": user.id,
            "username": user.username,
            "token": token.key
        })

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    "user_id": user.id,
                    "username": user.username,
                    "token": token.key
                })
            return Response({"error": "Invalid Credentials"}, status=400)
        return Response(serializer.errors, status=400)


class FollowView(APIView):
    def post(self, request, user_id):
        follower = request.user
        try:
            following_user = CustomUser.objects.get(id=user_id)
            if follower == following_user:
                return Response({"error": "You cannot follow yourself."}, status=400)
            follow_relation, created = following.objects.get_or_create(user=follower, following_user=following_user)
            if created:
                return Response({"status": f"You are now following {following_user.username}."})
            else:
                follow_relation.delete()
                return Response({"status": f"You have unfollowed {following_user.username}."})
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist."}, status=404)