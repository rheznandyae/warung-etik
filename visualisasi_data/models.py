from django.db import models

class Transaksi(models.Model):
    jenis_transaksi = models.CharField(max_length=200)
    num_users = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.jenis_transaksi, self.num_users) 