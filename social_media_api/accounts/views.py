from django.shortcuts import render
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Post, Comment


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


from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = '/'

class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'
class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detailview.html'
class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_createview.html'
class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment_updateview.html'
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_deleteview.html'
    success_url = '/'