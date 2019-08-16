from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet
from comments.views import CommentViewSet
from users.views import UserViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, 'post')
router.register(r'comments', CommentViewSet, 'comment')
router.register(r'users', UserViewSet, 'user')

urlpatterns = router.urls
