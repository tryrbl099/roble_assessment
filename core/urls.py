
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/v1/',include('djoser.urls')),
    path('api/v1/',include('djoser.urls.authtoken')),
    
    path('auth/',include('user.urls')),
    path('admin/', admin.site.urls),
]
