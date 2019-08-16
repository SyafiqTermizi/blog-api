from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('config.api')),
    path('api/auth/', include('authentication.urls'))
]
