import requests
from django.conf import settings
from django.utils.http import urlencode
from rest_framework import generics, status
from rest_framework.response import Response

from books.api.serializers import BookSerializer
from books.models import Book


class BooksView(generics.ListCreateAPIView):
    queryset = Book.active_objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response = {
            'status_code': status.HTTP_200_OK,
            'status': 'success',
            'data': serializer.data
        }
        return Response(response)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = {
            'status_code': status.HTTP_201_CREATED,
            'status': 'success',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.active_objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = 'book_id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = {
            'status_code': status.HTTP_200_OK,
            'status': 'success',
            'data': serializer.data
        }
        return Response(response)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        response = {
            'status_code': status.HTTP_200_OK,
            'status': 'success',
            'message': f'The book {instance.name} was updated successfully',
            'data': serializer.data
        }
        return Response(response)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        response = {
            'status_code': status.HTTP_204_NO_CONTENT,
            'status': 'success',
            'message': f'The book {instance.name} was deleted successfully',
            'data': []
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)


class ExternalBooksView(generics.ListAPIView):
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        params = urlencode({'name': self.request.query_params.get('name', '')})
        response = requests.get(settings.ICE_FIRE_API, params=params)
        books_data = response.json()
        books = []
        for book in books_data:
            book.pop('url')
            book.pop('mediaType')
            book.pop('characters')
            book.pop('povCharacters')
            book['number_of_pages'] = book.pop('numberOfPages')
            book['release_date'] = book.pop('released')
            books.append(book)
        return Response({'status_code': status.HTTP_200_OK, "status": "success", 'data': books})
