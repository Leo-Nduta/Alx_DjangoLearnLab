*Code used to update objects in Django Shell:*
book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book

*Output:*
<Book: Nineteen Eighty-Four by George Orwell in 1949>
