from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.exceptions import ValidationError

from django.contrib.auth import get_user_model
from django.urls import reverse

from authentication.views import CustomAuthToken

UserModel = get_user_model()


class TestCustomAuthTokenViews(APITestCase):
    fixtures = ['db.json']

    def test_post(self):
        request = APIRequestFactory()
        request.data = {'username': 'admin', 'password': 'password123321'}

        view = CustomAuthToken()

        response = view.post(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'admin')
        self.assertEqual(response.data['email'], 'admin@example.com')

    def test_post_invalid(self):
        request = APIRequestFactory()
        request.data = {'username': 'test', 'password': 'test'}

        view = CustomAuthToken()

        with self.assertRaises(ValidationError):
            response = view.post(request)
