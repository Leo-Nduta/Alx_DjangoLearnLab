from django.shortcuts import render
from posts.models import Like
from rest_framework import generics, permissions, status
from rest_framework.response import Response

# Create your views here.
class LikeViewSet(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    
    def post(self, request, post_id):
        user = request.user
        try:
            like, created = Like.objects.get_or_create(user=user, post_id=post_id)
            if created:
                return Response({"status": "Post liked."}, status=status.HTTP_201_CREATED)
            #else:
                like.delete()
                return Response({"status": "Post unliked."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UnlikeViewSet(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, post_id):
        user = request.user
        try:
            like = Like.objects.get(user=user, post_id=post_id)
            like.delete()
            return Response({"status": "Post unliked."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"error": "Like does not exist."}, status=status.HTTP_404_NOT_FOUND)

class NotificationViewSet(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('is_read', '-time_stamp')