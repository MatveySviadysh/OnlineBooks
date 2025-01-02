from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from .models import Book
from .serializers import BookSerializer


class BookViewSetTest(APITestCase):
    def setUp(self):
        """Создаем тестовые данные"""
        self.book1 = Book.objects.create(
            title="Test Book 1",
            author="Author 1",
            description="Description 1",
            publication_date="2025-01-01",
            genre="Fiction",
            isbn="1234567890",
            pages=300,
            language="English",
            publisher="Publisher 1",
            available=True,
        )
        self.book2 = Book.objects.create(
            title="Test Book 2",
            author="Author 2",
            description="Description 2",
            publication_date="2025-01-02",
            genre="Fantasy",
            isbn="0987654321",
            pages=200,
            language="French",
            publisher="Publisher 2",
            available=False,
        )
        self.valid_data = {
            "title": "New Test Book",
            "author": "Author 3",
            "description": "New Description",
            "publication_date": "2025-01-03",
            "genre": "Non-Fiction",
            "isbn": "1122334455",
            "pages": 400,
            "language": "German",
            "publisher": "Publisher 3",
            "available": True,
        }

    @patch('books.producer.publish')
    def test_list_books(self, mock_publish):
        """Тестирование получения списка книг"""
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        mock_publish.assert_called_once_with(method='list', body={'message': 'Books list requested'})

    @patch('books.producer.publish')
    def test_retrieve_book(self, mock_publish):
        """Тестирование получения книги по ID"""
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
        mock_publish.assert_called_once_with(method='retrieve', body={'message': f'Book {self.book1.id} retrieved'})

    @patch('books.producer.publish')
    def test_create_book(self, mock_publish):
        """Тестирование создания книги"""
        response = self.client.post('/api/books/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        mock_publish.assert_called_once_with(method='create', body={'message': 'New book created', 'data': self.valid_data})

    @patch('books.producer.publish')
    def test_update_book(self, mock_publish):
        """Тестирование обновления книги"""
        updated_data = self.valid_data.copy()
        updated_data['title'] = "Updated Test Book"
        response = self.client.put(f'/api/books/{self.book1.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Test Book")
        mock_publish.assert_called_once_with(method='update', body={'message': f'Book {self.book1.id} updated', 'data': updated_data})

    @patch('books.producer.publish')
    def test_destroy_book(self, mock_publish):
        """Тестирование удаления книги"""
        response = self.client.delete(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
        mock_publish.assert_called_once_with(method='destroy', body={'message': f'Book {self.book1.id} deleted'})
