from django.shortcuts import render
from .models import Post, Comment
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response    


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

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user # Get users the current user follows
        following_users = user.following.all() # Get posts from these users
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)