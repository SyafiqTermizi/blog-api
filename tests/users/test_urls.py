from unittest import TestCase

from django.urls import reverse, resolve


class TestUserUrls(TestCase):

    def test_list(self):
        self.assertEqual(reverse('user-list'), '/api/users/')
        self.assertEqual(resolve('/api/users/').view_name, 'user-list')

    def test_detail(self):
        self.assertEqual(reverse('user-detail', kwargs={'pk':1}), '/api/users/1/')
        self.assertEqual(resolve('/api/users/1/').view_name, 'user-detail')
