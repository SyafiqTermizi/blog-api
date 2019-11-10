from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

from django.utils import timezone

from comments.models import Comment

from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def get_queryset(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return Post.objects.filter(created_by=self.request.user)
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def list(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            response = super().list(request, *args, **kwargs).data
            if self.request.GET.get('limit'):
                response = response['results']
            return Response(
                {'data': response},
                template_name='posts/list.html'
            )
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            response = super().retrieve(request, *args, **kwargs)
            comments = Comment.objects.filter(post=Post(pk=response.data['pk']))
            return Response(
                {'data': response.data, 'comments': comments},
                template_name='posts/detail.html'
            )
        return super().retrieve(request, *args, **kwargs)
