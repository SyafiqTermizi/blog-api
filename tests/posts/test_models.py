from django.test import TestCase

from posts.models import Post


class TestPostModel(TestCase):
    fixtures = ['db.json']

    def test_ordering(self):
        self.assertTrue(
            Post.objects.first().created_at > Post.objects.last().created_at
        )

    def test_str(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.title, post.__str__())
