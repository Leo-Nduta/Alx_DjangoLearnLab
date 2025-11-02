*Code used to delete objects in Django Shell:*

Error code:
book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete
<bound method Model.delete of <Book: Nineteen Eighty-Four by George Orwell in 19
49>>
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell in 1949>]>

Correct code:
>>> book = Book.objects.get(title = "Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
