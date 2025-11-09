from django.urls import path
from .views import (
    LibraryDetailView,
    register, login_user, logout_user,
    admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book
)
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
]