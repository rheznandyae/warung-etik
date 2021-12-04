from django.http import response
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Transaksi

# Create your views here.


def pembayaran(request):

    if request.method == 'POST':

        metode = request.POST.get('metode')

        lastTR = Transaksi.objects.last()

        if lastTR == None:
            newID = 'TR00001'

        else:
            lastID = int(lastTR.idTransaksi[2:])
            # print(lastID)
            newID = lastID + 1
            # print(newID)

            if newID < 10:
                newID = 'TR0000' + str(newID)
            elif newID < 100:
                newID = 'TR000' + str(newID)
            elif newID < 1000:
                newID = 'TR00' + str(newID)
            elif newID < 10000:
                newID = 'TR0' + str(newID)
            else:
                newID = 'TR' + str(newID)

        newTR = Transaksi(
            idTransaksi = newID,
            statusTransaksi = 'menunggu konfirmasi pembayaran',
            usernamePembeli = 'tes',
            caraPembayaran = metode,
            timeStamp = timezone.now()
        )

        newTR.save()

        # print(newID)
    
        return redirect('transaksi:transaksiBayar')
    
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

