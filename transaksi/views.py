from django.http import response
from django.shortcuts import render

def pembayaran(request):
    context = {}
    return render(request, 'pembayaran.html', context=context)

def transaksiBayar(request):
    context = {}
    return render(request, 'transaksi-bayar.html', context=context)

def transaksiKonfirm(request):
    context = {}
    return render(request, 'transaksi-konfirm.html', context=context)

def transaksiDone(request):
    context = {}
    return render(request, 'transaksi-done.html', context=context)

def transaksiFailTemp(request):
    context = {}
    return render(request, 'transaksi-failtemp.html', context=context)

# Create your views here.
