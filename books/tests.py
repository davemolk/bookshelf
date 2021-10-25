from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='dave',
            email='dave@bookshelf.com',
            password='testpass123',
        )
        self.book = Book.objects.create(
            title='Black Hat Python',
            author='Justin Seitz',
            notes='what fun!',
            cover_url='https://www.python.org/static/img/python-logo@2x.png',
            owner = self.user,
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Black Hat Python')
        self.assertEqual(f'{self.book.author}', 'Justin Seitz')
        self.assertEqual(f'{self.book.notes}', 'what fun!')
        self.assertEqual(f'{self.book.cover_url}', 'https://www.python.org/static/img/python-logo@2x.png')
        self.assertEqual(f'{self.book.owner}', self.user.username)

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email='dave@bookshelf.com', password='testpass123')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Black Hat Python')
        self.assertTemplateUsed(response, 'books/book_list.html')
