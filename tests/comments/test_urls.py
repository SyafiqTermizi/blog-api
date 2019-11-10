from unittest import TestCase

from django.urls import reverse, resolve


class TestCommentUrls(TestCase):

    def test_list(self):
        self.assertEqual(reverse('comment-list'), '/comments/')
        self.assertEqual(resolve('/comments/').view_name, 'comment-list')

    def test_detail(self):
        self.assertEqual(reverse('comment-detail', kwargs={'pk': 1}), '/comments/1/')
        self.assertEqual(resolve('/comments/1/').view_name, 'comment-detail')
