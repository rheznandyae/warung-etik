from django.urls import path

from . import views

app_name = 'keranjang'

urlpatterns = [
    path('', views.keranjang_view, name='keranjang'),
    # path('api/', views.base_api, name='base'),
    path('api/getbyusername/<str:username>/', views.get_item_keranjang_by_user, name='getItemKeranjangByUser'),
    path('api/createitemkeranjang/', views.create_item_keranjang, name="createItemKeranjang"),
    path('api/plus1/', views.plus1_amount_item_keranjang, name="plus1"),
    path('api/minus1/', views.minus1_amount_item_keranjang, name="minus1"),
    path('api/<int:id_keranjang>', views.item_keranjang_detail, name="item_keranjang_detail"),
    path('api/gettotalprice/<str:username>', views.get_total_price, name="get_total_price")

]
