from unittest import TestCase

from django.urls import resolve, reverse


class TestAuthenticationUrls(TestCase):

    def test_get_token(self):
        self.assertEqual(reverse('authentication:auth'), '/api/auth/')
        self.assertEqual(resolve('/api/auth/').view_name, 'authentication:auth')