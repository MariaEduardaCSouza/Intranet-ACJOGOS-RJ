from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('', views.home, name='home'),
    path('auth/', include('authentication.urls')),
    ]


