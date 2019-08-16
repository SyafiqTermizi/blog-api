from django.test import TestCase

from comments.models import Comment


class TestPostModel(TestCase):
    fixtures = ['db.json']

    def test_ordering(self):
        self.assertTrue(
            Comment.objects.first().created_at > Comment.objects.last().created_at
        )
