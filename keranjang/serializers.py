from django.contrib.auth import models
from rest_framework import serializers

from admin_warung.models import Barang
from .models import ItemKeranjang

class BarangSerializers(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = ['nama', 'deskripsi', 'harga','image_url']

class ItemKeranjangSerializers(serializers.ModelSerializer):
    barang = BarangSerializers(read_only=True)
    class Meta:
        model = ItemKeranjang
        fields = ['id', 'barang','jumlah_item']
