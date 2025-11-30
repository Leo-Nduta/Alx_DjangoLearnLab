from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class BookPermission(IsAuthenticatedOrReadOnly):
    pass

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'publication_year', 'author__name']
    
    # ENABLE FILTERING, SEARCHING, ORDERING
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtering options ?title= ?publication_year= ?author=
    filterset_fields = ['title', 'publication_year', 'author']

    # Search across title and author name
    search_fields = ['title', 'author__name']

    # Allow ordering via ?ordering=title or ?ordering=-publication_year
    ordering_fields = ['title', 'publication_year', 'author']
    ordering = ['title']  # default ordering

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    def perform_create(self, serializer):
        """
        Custom logic before saving.
        We can log, enforce rules, or attach the user if necessary.
        """
        # Example: Print debug info (you can remove in production)
        print("Creating a book:", serializer.validated_data)

        serializer.save()  # Saves the book after validation

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_update(self, serializer):
        """
        Additional update logic can go here.
        """
        print("Updating a book:", serializer.validated_data)
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]