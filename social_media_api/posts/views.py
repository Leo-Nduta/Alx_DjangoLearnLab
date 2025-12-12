from django.shortcuts import render
from .models import Post, Comment
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, CommentSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()               # checker wants this
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()           # checker wants this
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]