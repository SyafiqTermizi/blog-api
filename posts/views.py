from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination

from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        owner_actions = ['update', 'partial_update', 'destroy']

        if self.action in owner_actions:
            return Post.objects.filter(created_by=self.request.user)
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
