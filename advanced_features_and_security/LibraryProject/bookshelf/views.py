from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        # Only users with can_create can reach this line
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('book_list')

    return render(request, "create_book.html")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_profile(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("book_list")

    return render(request, "edit_book.html", {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_profile(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')