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
    
        return redirect('transaksi:transaksiChecker', id = newID)
        # return redirect('/transaksi/temp/?id=' + newID + '/')
    
    context = {}
    return render(request, 'pembayaran.html', context)


def transaksiChecker(request, id):

    TR = Transaksi.objects.get(idTransaksi = id)

    context = {'transaksi':TR}

    if request.method == 'POST':
        
        action = request.POST.get('action')

        if action == 'konfirmasi':
            TR.statusTransaksi = 'menunggu konfirmasi admin'

            TR.save()

            print('tested tit')

            return render(request, 'transaksi-konfirm.html', context)

        elif action == 'batal':
            TR.statusTransaksi = 'transaksi dibatalkan'

            TR.save()

            print('tested tot')

            return render(request, 'transaksi-done.html', context)

    if request.method == 'GET':

        status = TR.statusTransaksi

        if status == 'menunggu konfirmasi pembayaran':
            return render(request, 'transaksi-bayar.html', context)

        elif status == 'menunggu konfirmasi admin':
            return render(request, 'transaksi-konfirm.html', context)

        else:
            return render(request, 'transaksi-done.html', context)







def transaksiBayar(request, ID):

    TR = Transaksi.objects.get(idTransaksi = ID)

    context = {'transaksi':TR}
    return render(request, 'transaksi-bayar.html', context)

def transaksiKonfirm(request):
    context = {}
    return render(request, 'transaksi-konfirm.html', context)

def transaksiDone(request):
    context = {}
    return render(request, 'transaksi-done.html', context)

def transaksiFailTemp(request):
    context = {}
    return render(request, 'transaksi-failtemp.html', context)
