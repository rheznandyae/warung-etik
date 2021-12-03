from django.db import models

# Create your models here.

class Barang(models.Model):
    nama = models.CharField(max_length=100)
    id_barang = models.IntegerField()
    harga = models.PositiveIntegerField()
    stok = models.PositiveIntegerField()
    terjual = models.PositiveIntegerField()
    deskripsi = models.TextField()