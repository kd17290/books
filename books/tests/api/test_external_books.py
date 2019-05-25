from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase


class TestExternalBooksAPI(APITestCase):
    def test_external_valid_response(self):
        url = reverse('api.books:external_books')
        params = urlencode({'name': 'A Game of Thrones'})
        url = f"{url}?{params}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(response_data['status_code'], 200)
        self.assertEqual(response_data['status'], "success")
        self.assertEqual(type(response_data['data']), list)
        self.assertEqual(len(response_data['data']), 1)

    def test_external_invalid_response(self):
        url = reverse('api.books:external_books')
        params = urlencode({'name': 'random'})
        url = f"{url}?{params}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data
        self.assertEqual(response_data['status_code'], 200)
        self.assertEqual(response_data['status'], "success")
        self.assertEqual(type(response_data['data']), list)
        self.assertEqual(len(response_data['data']), 0)
