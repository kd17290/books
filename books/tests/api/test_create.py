from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book


class TestCreateBookAPI(APITestCase):
    def test_create(self):
        url = reverse('api.books:books')
        data = {
            "name": "My First Book",
            "isbn": "123-3213243567",
            "authors": [
                "John Doe"
            ],
            "number_of_pages": 350,
            "publisher": "Acme Books Publishing",
            "country": "United States",
            "release_date": "2019-01-01"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = response.data
        self.assertEqual(response_data['status_code'], status.HTTP_201_CREATED)
        self.assertEqual(response_data['status'], 'success')
        id = response_data['data'].pop('id')
        self.assertEqual(response_data['data'], data)
        book = Book.objects.get(pk=id)
        self.assertEqual(book.name, data.get('name'))
        self.assertEqual(book.isbn, data.get('isbn'))
        self.assertEqual(book.number_of_pages, data.get('number_of_pages'))
        self.assertEqual(list(book.authors.values_list('name', flat=True)), data.get('authors'))
