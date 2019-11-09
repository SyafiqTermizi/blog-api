from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('config.api')),
    path('api/auth/', include('authentication.urls'))
]
