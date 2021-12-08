from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('admin/', views.chat_admin, name='chat_admin'),
    # path('pelanggan/', views.chat_pelanggan, name='chat_pelanggan'),
]
