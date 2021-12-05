from django.db import models

class Barang(models.Model):
    nama = models.CharField(max_length=100)
    # id_barang = models.IntegerField(blank=True, null=True)
    harga = models.PositiveIntegerField(blank=True, null=True)
    stok = models.PositiveIntegerField(blank=True, null=True)
    terjual = models.PositiveIntegerField(blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)
    image_url= models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return "{}-{}".format(self.nama, self.id)
