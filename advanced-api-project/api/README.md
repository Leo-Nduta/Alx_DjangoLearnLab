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