from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestListEmptyBookAPI(APITestCase):

    def test_retrieve(self):
        url = reverse('api.books:books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data
        self.assertEqual(response_data['status_code'], status.HTTP_200_OK)
        self.assertEqual(response_data['status'], 'success')
        self.assertEqual(len(response_data['data']), 0)


class TestListBookAPI(APITestCase):
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

    def setUp(self) -> None:
        url = reverse('api.books:books')
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.id = response.json()['data']['id']

    def test_retrieve(self):
        url = reverse('api.books:books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data
        self.assertEqual(response_data['status_code'], status.HTTP_200_OK)
        self.assertEqual(response_data['status'], 'success')
        self.assertEqual(len(response_data['data']), 1)
        data = response_data['data'][0]
        data.pop('id')
        self.assertEqual(data, self.data)
