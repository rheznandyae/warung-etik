from django.db import models
from django.db.models.deletion import CASCADE
from admin_warung.models import Barang
from django.contrib.auth.models import User

class ReviewBarang(models.Model):
    barang = models.ForeignKey(Barang, related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    bintang = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)