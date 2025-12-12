from django.contrib import admin
from django.urls import path
from accounts import views
from .views import PostCreateView, PostDetailView, PostListView, PostUpdateView, PostDeleteView, CommentCreateView, CommentDetailView, CommentListView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('/post/new/', PostCreateView.as_view(), name='create_post'),
    path('/post/<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
    path('/post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('/post/<int:pk>/', PostDetailView.as_view(), name = 'view_post'),
    path('/post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='create_comment'),
    path('/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update_comment'),
    path('/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('/comment/<int:pk>/', CommentDetailView.as_view(), name = 'view_comment'),
]