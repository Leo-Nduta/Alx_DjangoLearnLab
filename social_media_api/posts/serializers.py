from rest_framework import serializers
from .models import Post, Comment
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        Model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.PrimaryKeyRelatedField(source='post.id', queryset = Post.objects.all())
    class Meta:
        Model = Comment
        fields = '__all__'