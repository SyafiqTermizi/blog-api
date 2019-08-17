from rest_framework.test import (
    APITestCase, APIClient, APIRequestFactory, force_authenticate
)
from django.contrib.auth import get_user_model
from django.http import Http404
from django.urls import reverse

from comments.views import CommentViewSet
from comments.models import Comment
from comments.serializers import CommentSerializer

UserModel = get_user_model()


class TestCommentViews(APITestCase):
    fixtures = ['db.json']

    def test_get_queryset_list(self):
        view = CommentViewSet()
        view.action = 'list'

        request = APIRequestFactory()
        request.get(reverse('comment-list'))
        request.query_params = {'user': 2, 'post': 1}

        force_authenticate(request, UserModel.objects.get(pk=1))

        view.request = request

        response = view.get_queryset()

        self.assertEqual(response.first().post_id, 1)
        self.assertEqual(response.last().post_id, 1)
        self.assertEqual(response.first().created_by_id, 2)
        self.assertEqual(response.last().created_by_id, 2)

    def test_get_queryset_list_user(self):
        view = CommentViewSet()
        view.action = 'list'

        request = APIRequestFactory()
        request.get(reverse('comment-list'))
        request.query_params = {'user': 2}

        force_authenticate(request, UserModel.objects.get(pk=1))

        view.request = request

        response = view.get_queryset()

        self.assertEqual(response.first().created_by_id, 2)
        self.assertEqual(response.last().created_by_id, 2)

    def test_get_queryset_list_post(self):
        view = CommentViewSet()
        view.action = 'list'

        request = APIRequestFactory()
        request.get(reverse('comment-list'))
        request.query_params = {'post': 1}

        force_authenticate(request, UserModel.objects.get(pk=1))

        view.request = request

        response = view.get_queryset()

        self.assertEqual(response.first().post_id, 1)
        self.assertEqual(response.last().post_id, 1)

    def test_get_queryset_list_404(self):
        view = CommentViewSet()
        view.action = 'list'

        request = APIRequestFactory()
        request.get(reverse('comment-list'))
        request.query_params = dict()

        force_authenticate(request, UserModel.objects.get(pk=1))

        view.request = request

        with self.assertRaises(Http404):
            response = view.get_queryset()

    def test_get_queryset_list_owner(self):
        view = CommentViewSet()
        view.action = 'update'

        request = APIRequestFactory()
        request.post('/api/comments/1/')

        user = UserModel.objects.get(pk=2)
        force_authenticate(request, user)

        request.user = user
        view.request = request

        response = view.get_queryset()

        self.assertEqual(response.last().created_by_id, 2)

    def test_perform_create(self):
        client = APIClient()
        client.login(username='admin', password='password123321')
        client.post(
            '/api/comments/?post=1',
            data={'title': 'test', 'body': 'test'},
            format='json'
        )
        c = Comment.objects.last()
        self.assertEqual(c.created_by_id, 1)

    def test_perform_create_404(self):
        view = CommentViewSet()
        view.action = 'create'

        request = APIRequestFactory()
        request.post(
            '/api/comments/?post=1/',
            data={'title': 'test', 'body': 'test'}
        )
        request.query_params = {}

        user = UserModel.objects.get(pk=1)
        force_authenticate(request, user)

        request.user = user
        view.request = request

        with self.assertRaises(Http404):
            response = view.perform_create(CommentSerializer)
