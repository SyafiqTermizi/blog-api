from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
