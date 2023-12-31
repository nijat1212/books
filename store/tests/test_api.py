from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from store.models import Book
from store.serializer import BookSerializer


class BooksApiTestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='Test Book1', price=23)
        book_2 = Book.objects.create(name='Test Book2', price=23)
        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        serializer_data = BookSerializer([book_1, book_2], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
