from unittest import TestCase

from django.urls import reverse, resolve


class TestCommentUrls(TestCase):

    def test_list(self):
        self.assertEqual(reverse('comment-list'), '/api/comments/')
        self.assertEqual(resolve('/api/comments/').view_name, 'comment-list')

    def test_detail(self):
        self.assertEqual(reverse('comment-detail', kwargs={'pk': 1}), '/api/comments/1/')
        self.assertEqual(resolve('/api/comments/1/').view_name, 'comment-detail')
