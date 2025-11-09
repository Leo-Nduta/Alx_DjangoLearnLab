from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.views import View

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html")

class DetailView(View):
    def get(self, **kwargs):
        library = Library.objects.get(id=kwargs['library_id'])
        return render('library_detail.html', {'library': library, 'books': library.books.all()})

