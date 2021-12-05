from django.db import models

# Create your models here.

class Barang(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.PositiveIntegerField(blank=True, null=True)
    stok = models.PositiveIntegerField(blank=True, null=True)
    terjual = models.PositiveIntegerField(blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama

    def snippet(self):
        return self.deskripsi[:150] + '...' if len(self.deskripsi) > 150 else self.deskripsi
    
    def get_all_value(self):
        return [field.value_from_object(self) for field in Barang._meta.fields]


