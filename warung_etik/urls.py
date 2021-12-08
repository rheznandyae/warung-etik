from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('keranjang/', include('keranjang.urls')),
    path('dashboard/', include('admin_warung.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('transaksi/', include('transaksi.urls', namespace='transaksi')),
    path('barang/', include('barang.urls', namespace='barang')),
    path('review/', include('review.urls', namespace='review')),
    path('visualisasi/', include('visualisasi_data.urls', namespace='visualisasi_data')),
  
]
