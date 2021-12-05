from django.db import models
from django.contrib.auth.models import User
from admin_warung.models import Barang
from transaksi.models import Transaksi
# Create your models here.

class ItemKeranjang(models.Model):
    pelanggan = models.ForeignKey(User, on_delete=models.CASCADE)
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE, null=True, blank=True)
    jumlah_item = models.BigIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return "{}-{}".format(self.pelanggan, self.barang)