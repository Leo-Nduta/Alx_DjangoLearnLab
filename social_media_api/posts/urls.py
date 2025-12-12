from django.urls import path, include
from .views import FeedView

urlpatterns = [
    path('', include(router.urls)),
    path('api', include('posts.urls')),
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='like_post'),
    path('posts/<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='unlike_post'),
]

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

