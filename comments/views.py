from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import Http404

from posts.models import Post

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        owner_actions = ['update', 'partial_update', 'destroy']

        if self.action == 'list':
            user = self.request.query_params.get('user', None)
            post = self.request.query_params.get('post', None)

            if user and post:
                return Comment.objects.filter(post__id=post).filter(created_by__id=user)
            elif user and not post:
                return Comment.objects.filter(created_by__id=user)
            elif post and not user:
                return Comment.objects.filter(post__id=post)
            raise Http404

        elif self.action in owner_actions:
            return Comment.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        post = self.request.query_params.get('post', None)

        if not post:
            raise Http404

        serializer.save(created_by=self.request.user, post=Post(pk=post))
