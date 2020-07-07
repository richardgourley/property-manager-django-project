# MAIN URL FILE - PROPERTIES URLS ADDED
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('properties/', include('properties.urls')),
    path('admin/', admin.site.urls),
]
