from unittest import TestCase

from django.urls import reverse, resolve


class TestPostUrls(TestCase):

    def test_list(self):
        self.assertEqual(reverse('post-list'), '/posts/')
        self.assertEqual(resolve('/posts/').view_name, 'post-list')

    def test_detail(self):
        self.assertEqual(reverse('post-detail', kwargs={'pk': 1}), '/posts/1/')
        self.assertEqual(resolve('/posts/1/').view_name, 'post-detail')
