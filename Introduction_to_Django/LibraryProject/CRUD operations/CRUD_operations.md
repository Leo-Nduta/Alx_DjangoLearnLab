This md document summarizes the CRUD operations done in create.md, retrieve.md, update.md and delete.md

In create.md, i imported the class Book and made the first input by using Book.objects.create then specifying values of all indicated functions

In retrieve.md I used Book.objects.get to retrieve values that were input previously.
I then used book.author to get the author value, book.publication_year to get the publication year value and book.title to obtain the book's title

In update.md I used Book.objects.get to retrieve the value i wish to update.
I then used Book.title = *updated title* to update from my old title.
I finished by saving it using Book.save()

In delete.md I used book = Book.objects.get(*title*) to retrieve the title of the book I wish to delete.
I then used Book.delete() to delete the retrieved book.
Note that Book.delete without the brackets just calls the delete function but doesn't do the deleting