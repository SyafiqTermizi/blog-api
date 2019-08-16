from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth import get_user_model

from .serializers import UserSerializer

UserModel = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
