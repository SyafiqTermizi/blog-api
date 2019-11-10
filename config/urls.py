from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('config.api')),
    path('auth/', include('rest_framework.urls')),
    path('api/auth/', include('authentication.urls'))
]
