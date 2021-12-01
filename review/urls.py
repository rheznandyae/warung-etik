from django.urls import path

from . import views

app_name = 'review'

urlpatterns = [
    path('tulis/', views.tulis, name='tulis'),
]
