from rest_framework.serializers import ModelSerializer
from rest_framework.fields import CharField

from .models import Comment


class CommentSerializer(ModelSerializer):
    created_by = CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ('body', 'created_by', 'created_at')
