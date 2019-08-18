from rest_framework.serializers import ModelSerializer, CurrentUserDefault
from rest_framework.fields import CharField, HiddenField


from .models import Post


class PostSerializer(ModelSerializer):
    created_by = CharField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('pk', 'title', 'body', 'created_by', 'created_at')
