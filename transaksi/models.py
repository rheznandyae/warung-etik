from django.db import models

# Create your models here.


class Transaksi(models.Model):

    idTransaksi = models.CharField(primary_key=True, max_length=100)

    timeStamp = models.DateTimeField(auto_now_add=True, null=True)

    statusTransaksi = models.CharField(null=False, max_length=100)

    usernamePembeli = models.CharField(null=False, max_length=100)

    caraPembayaran = models.CharField(null=False, max_length=100)

    totalPesanan = models.PositiveIntegerField(null=False, default=0)