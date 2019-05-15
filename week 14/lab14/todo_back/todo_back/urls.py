
from django.contrib import admin
from django.urls import path, include
import api
import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
