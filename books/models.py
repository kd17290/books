from django.db import models

from books.managers import ActiveObjectsManager


class Audit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class SoftDelete(models.Model):
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        abstract = True


class Author(Audit, SoftDelete):
    name = models.CharField(max_length=50)


class Publisher(Audit, SoftDelete):
    name = models.CharField(max_length=50)


class Country(Audit, SoftDelete):
    name = models.CharField(max_length=50)


class Book(Audit, SoftDelete):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    authors = models.ManyToManyField(Author, related_name='books')
    number_of_pages = models.SmallIntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='books')
    release_date = models.DateField()
