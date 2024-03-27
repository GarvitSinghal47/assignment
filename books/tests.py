# books/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book


class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(
            title='Test Book', authors='Test Author', isbn='1234567890123')

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_book(self):
        data = {'title': 'New Book',
                'authors': 'New Author', 'isbn': '9876543210987'}
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
