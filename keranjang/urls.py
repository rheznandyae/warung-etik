from django.urls import path

from . import views

app_name = 'keranjang'

urlpatterns = [
    path('', views.keranjang_view, name='keranjang'),
]
