from django.urls import path

from . import views

app_name = 'admin_warung'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('detail-barang/<int:id>/', views.detail_barang_admin_view, name='detail-barang-admin'),
    path('hapus-barang/<int:id>/', views.hapus_barang_view, name='hapus-barang'),
    path('tambah-barang', views.tambah_barang_view, name='tambah-barang'),
    path('ubah-barang/<int:id>/', views.ubah_barang_view, name='ubah-barang'),
    path('list-ubah', views.list_ubah_view, name='list-ubah'),
    path('list-hapus', views.list_hapus_view, name='list-hapus'),
    path('import-barang', views.import_barang, name='import-barang')
]
