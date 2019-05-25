from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book


class TestCreateBookAPI(APITestCase):
    def setUp(self) -> None:
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
        self.id = response.data['data']['id']

    def test_update(self):
        url = reverse('api.books:book_detail', kwargs={'book_id': self.id})
        data = {
            "name": "My First Updated Book",
            "isbn": "123-3213243567",
            "authors": [
                "John Doe"
            ],
            "number_of_pages": 350,
            "publisher": "Acme Books Publishing",
            "country": "United States",
            "release_date": "2019-01-01"
        }
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data
        self.assertTrue('message' in response_data)
        self.assertEqual(response_data['status_code'], status.HTTP_200_OK)
        self.assertEqual(response_data['status'], 'success')
        response_data['data'].pop('id')
        self.assertEqual(response_data['data'], data)
        book = Book.objects.get(pk=self.id)
        self.assertEqual(book.name, data['name'])
