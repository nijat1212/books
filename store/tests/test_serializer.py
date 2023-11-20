from django.test import TestCase
from store.models import Book
from store.serializer import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test Book1', price=23)
        book_2 = Book.objects.create(name='Test Book2', price=23)
        data = BookSerializer([book_1, book_2], many=True).data
        excepted_data = [
            {
                'id': book_1.id,
                'name': 'Test Book1',
                'price': '23.00'
            },
            {
                'id': book_2.id,
                'name': 'Test Book2',
                'price': '23.00'
            },
        ]
        self.assertEqual(excepted_data, data)
