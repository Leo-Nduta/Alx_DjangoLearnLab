from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    try:
        author = Author.objects.get(name = author_name)
        books = Book.objects.filter(author = author)
        return books
    except Author.DoesNotExist:
        return f"No author found with name: {author_name}"

def books_in_library(library_name):
    try:
        library = Library.objects.get(name = library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return f"No library found with name: {library_name}"

def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name = library_name)
        return library.librarian
    except Library.DoesNotExist:
        return f"No library found with name: {library_name}"