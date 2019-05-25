from rest_framework import serializers

from books.api.fields import FKField
from books.models import Book, Publisher, Country, Author


class BookSerializer(serializers.ModelSerializer):
    publisher = FKField(queryset=Publisher.objects.all())
    country = FKField(queryset=Country.objects.all())
    authors = FKField(many=True, queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'name', 'isbn', 'authors', 'number_of_pages', 'publisher', 'country', 'release_date')
