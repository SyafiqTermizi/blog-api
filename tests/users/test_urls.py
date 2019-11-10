from unittest import TestCase

from django.urls import reverse, resolve


class TestUserUrls(TestCase):

    def test_list(self):
        self.assertEqual(reverse('user-list'), '/users/')
        self.assertEqual(resolve('/users/').view_name, 'user-list')

    def test_detail(self):
        self.assertEqual(reverse('user-detail', kwargs={'pk':1}), '/users/1/')
        self.assertEqual(resolve('/users/1/').view_name, 'user-detail')
