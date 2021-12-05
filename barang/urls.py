from django.urls import path

from . import views

app_name = 'barang'

urlpatterns = [
    path('detail/<int:id>/', views.detail_barang, name='detail'),
]
