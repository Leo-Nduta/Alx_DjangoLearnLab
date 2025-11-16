*Code used to create in Django shell:*
from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication
_year=1949)
>>> book

*Output:*
<Book: 1984 by George Orwell in 1949>
