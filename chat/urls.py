from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('check/', views.check, name='check'),
    
    
    path('admin/', views.chat_admin, name='chat_admin'),
]
