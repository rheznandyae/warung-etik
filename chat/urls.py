from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'chat'

urlpatterns = [
    path('admin/', views.chat_admin, name='chat_admin'),
    path('pelanggan/', views.chat_pelanggan, name='chat_pelanggan'),
]
