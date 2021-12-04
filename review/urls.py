from django.urls import path

from . import views

app_name = 'review'

urlpatterns = [
    path('tulis/<int:id>/', views.tulis, name='tulis'),
]
