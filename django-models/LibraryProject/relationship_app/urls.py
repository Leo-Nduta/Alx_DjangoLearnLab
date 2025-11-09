from django.contrib import admin
from django.urls import path, include
from relationship_app.views import list_books, DetailView
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
    path('books/', list_books, name='list_books'),
    path('library/<int:library_id>/', DetailView.as_view(), name='library_detail'),
    path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library_detail'),
]