from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('nvaadmin/', admin.site.urls, name="admin"),
    path('', include('bible_api.urls')),
]