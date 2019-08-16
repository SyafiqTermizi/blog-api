from unittest import TestCase

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class TestUserModel(TestCase):

    def test_str(self):
        user = UserModel(username='test')
        self.assertEqual(user.__str__(), 'test')
