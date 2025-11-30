from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

from api.models import Book, Author


class BookAPITestCase(APITestCase):
    """
    Test Suite for Book API CRUD operations,
    filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        # Create user for authentication
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(
            title="Django Unleashed",
            publication_year=2020,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Python Basics",
            publication_year=2021,
            author=self.author2
        )

        # APIClient for authenticated tests
        self.client = APIClient()

    # ----------------------------
    #       CRUD TESTS
    # ----------------------------

    def test_list_books(self):
        """Ensure we can list books"""
        response = self.client.get(reverse("book-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """Retrieve a single book by ID"""
        response = self.client.get(reverse("book-detail", args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django Unleashed")

    def test_create_book_authenticated(self):
        """Authenticated users should be able to create a book"""
        self.client.login(username="testuser", password="password123")

        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author1.id
        }
        response = self.client.post(reverse("book-create"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users should NOT be able to create a book"""
        data = {
            "title": "Should Fail",
            "publication_year": 2022,
            "author": self.author1.id
        }
        response = self.client.post(reverse("book-create"), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Authenticated user can update book"""
        self.client.login(username="testuser", password="password123")

        data = {
            "title": "Updated Title",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.put(reverse("book-update", args=[self.book1.id]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """Authenticated user can delete a book"""
        self.client.login(username="testuser", password="password123")

        response = self.client.delete(reverse("book-delete", args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # ----------------------------
    #    FILTERING / SEARCH / ORDER
    # ----------------------------

    def test_filter_books_by_publication_year(self):
        response = self.client.get("/books/?publication_year=2021")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Python Basics")

    def test_search_books(self):
        response = self.client.get("/books/?search=Django")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django Unleashed")

    def test_order_books_descending(self):
        response = self.client.get("/books/?ordering=-publication_year")
        self.assertEqual(response.data[0]["publication_year"], 2021)


    # ----------------------------
    #      PERMISSION TESTS
    # ----------------------------

    def test_unauthenticated_update_forbidden(self):
        """Unauthenticated users CANNOT update"""
        data = {
            "title": "Hack Attempt",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.put(reverse("book-update", args=[self.book1.id]), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_delete_forbidden(self):
        """Unauthenticated users CANNOT delete"""
        response = self.client.delete(reverse("book-delete", args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
