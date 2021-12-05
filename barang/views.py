from django.http import response
from django.shortcuts import get_object_or_404, render
from admin_warung.models import Barang

def detail_barang(request, id):
    barang = get_object_or_404(Barang, id=id)
    context = {
        "barang":barang
    }
    return render(request, 'detail-barang.html', context)
