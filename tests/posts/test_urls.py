from unittest import TestCase

from django.urls import reverse, resolve


class TestPostUrls(TestCase):

    def test_list(self):
        self.assertEqual(reverse('post-list'), '/api/posts/')
        self.assertEqual(resolve('/api/posts/').view_name, 'post-list')

    def test_detail(self):
        self.assertEqual(reverse('post-detail', kwargs={'pk': 1}), '/api/posts/1/')
        self.assertEqual(resolve('/api/posts/1/').view_name, 'post-detail')
