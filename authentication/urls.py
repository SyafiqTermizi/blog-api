from django.urls import path

from .views import CustomAuthToken


app_name = 'authentication'
urlpatterns = [
    path('', CustomAuthToken.as_view(), name='auth')
]
