from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model

from posts.views import PostViewSet
from posts.models import Post

UserModel = get_user_model()


class TestPostViews(APITestCase):
    fixtures = ['db.json']

    def test_get_queryset(self):
        view = PostViewSet()
        view.action = 'list'

        response = view.get_queryset()

        self.assertEquals(list(Post.objects.all()), list(response))

    def test_get_queryset_owner(self):
        user = UserModel.objects.get(pk=2)

        request = APIRequestFactory()
        request.user = user

        view = PostViewSet()
        view.action = 'update'
        view.request = request

        response = view.get_queryset()
        self.assertEqual(response.first().created_by, user)
        self.assertEqual(response.last().created_by, user)

    def test_perform_create(self):
        client = APIClient()
        client.login(username='admin', password='password123321')
        client.post(
            '/api/posts/',
            data={'title': 'test', 'body': 'test'},
            format='json'
        )
        p = Post.objects.first()
        self.assertEqual(p.created_by_id, 1)
