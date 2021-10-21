from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='dave',
            email='dave@example.com',
            password='testpass123',
        )
        self.assertEqual(user.username, 'dave')
        self.assertEqual(user.email, 'dave@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superdave',
            email='superdave@example.com',
            password='testpass123',
        )
        self.assertEqual(admin_user.username, 'superdave')
        self.assertEqual(admin_user.email, 'superdave@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

