from django.http import response
from django.shortcuts import render

def detail_barang(request):
    context = {}
    return render(request, 'detail-barang.html', context=context)
