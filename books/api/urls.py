from django.urls import path

from books.api import views

urlpatterns = [
    path('<int:book_id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('external-books/', views.ExternalBooksView.as_view(), name='external_books'),
    path('', views.BooksView.as_view(), name='books')
]
