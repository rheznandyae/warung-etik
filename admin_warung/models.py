from django.db import models

# Create your models here.

class Barang(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.PositiveIntegerField()
    stok = models.PositiveIntegerField()
    terjual = models.PositiveIntegerField()
    deskripsi = models.TextField()
    image_url = models.TextField(default="")

    def __str__(self):
        return self.nama

    def snippet(self):
        return self.deskripsi[:150] + '...' if len(self.deskripsi) > 150 else self.deskripsi