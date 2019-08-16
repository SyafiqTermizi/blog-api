from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username
