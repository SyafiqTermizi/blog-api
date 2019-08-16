from django.db import models
from django.contrib.auth import get_user_model

from posts.models import Post

UserModel = get_user_model()


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        UserModel(),
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        ordering = ['-created_at']