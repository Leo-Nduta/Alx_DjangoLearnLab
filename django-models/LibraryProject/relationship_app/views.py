from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.views import View

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html")

from .models import Library
class DetailView(View):
    def get(self, **kwargs):
        library = Library.objects.get(id=kwargs['library_id'])
        return render("relationship_app/library_detail.html")

