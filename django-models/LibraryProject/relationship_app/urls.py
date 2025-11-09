from django.urls import path
from relationship_app.views import list_books, DetailView
from .views import list_books, LibraryDetailView, login_user, logout_user, register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('register/', register, name='register'),
]