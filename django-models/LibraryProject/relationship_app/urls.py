from django.urls import path
from relationship_app.views import list_books, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
    path('register/', views.register, name='register'),
    path('library/<int:library_id>/', views.LibraryDetailView.as_view(), name='library_detail'),
]