from django.urls import path

from . import views

app_name = 'transaksi'

urlpatterns = [
    path('', views.pembayaran, name='pembayaran'),
    path('payment/', views.transaksiBayar, name='transaksiBayar'),
    path('confirmation/', views.transaksiKonfirm, name='transaksiKonfirm'),
    path('done/', views.transaksiDone, name='transaksiDone'),
    path('fail/', views.transaksiFailTemp, name='transaksiFailTemp'),
    path('<str:id>/', views.transaksiChecker, name='transaksiChecker'),
]