Book API — View Documentation
Views Used

This API uses Django REST Framework Generic Views, enhanced with:

Custom validation (via perform_create, perform_update)

Authentication and permission checks

Optional filtering using SearchFilter

Detailed comments inside each class

Permissions

ListView & DetailView → Public access

Create, Update, Delete → Authenticated users only

Custom Logic

perform_create() logs and processes extra logic before saving a book

perform_update() handles additional validation or hooks

Custom BookPermission uses IsAuthenticatedOrReadOnly

Filtering

Users can filter books using:

?search=keyword


Search applies to:

title

publication_year

author name


TASK 2
📘 Advanced Query Capabilities for Book API

The BookListView supports:

✅ Filtering

You can filter books using any of the fields:

title

publication_year

author (by id)

Examples:

/books/?title=Inferno
/books/?author=2
/books/?publication_year=2020

🔍 Searching

Searches through:

title

author name

Examples:

/books/?search=python
/books/?search=rowling

🧭 Ordering

Sort results using:

title

publication_year

author

Examples:

/books/?ordering=title
/books/?ordering=-publication_year

🧪 Combined Example
/books/?search=django&publication_year=2023&ordering=-title

⚙️ Filters Enabled Through DRF