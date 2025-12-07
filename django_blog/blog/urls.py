from django.contrib import admin
from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views
from .views import PostCreateView, PostDetailView, PostListView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('/post/new/', PostCreateView.as_view(), name='create_post'),
    path('/post/<int:pk>/edit/', PostUpdateView.as_view(), name='update_post'),
    path('/posts/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('/posts/<int:pk>/', PostDetailView.as_view(), name = 'view_post'),
]