from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass', email='admin@test.com')

        # Authenticate client
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create initial Book
        self.book = Book.objects.create(title='Test Book', author='John Doe', description='Sample Description')

    def test_list_books(self):
        url = reverse('book-list')  # Ensure your URL names are set correctly in api/urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', str(response.data))

    def test_create_book_authenticated(self):
        url = reverse('book-list')
        data = {'title': 'New Book', 'author': 'Jane Doe', 'description': 'New Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        self.client.logout()
        url = reverse('book-list')
        data = {'title': 'Unauthorized Book', 'author': 'Unknown', 'description': 'Should Fail'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {'title': 'Updated Book', 'author': 'John Doe', 'description': 'Updated Description'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?search=Test'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Test Book' in str(book) for book in response.data))

    def test_permissions_admin_delete(self):
        self.client.logout()
        self.client.login(username='admin', password='adminpass')
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
