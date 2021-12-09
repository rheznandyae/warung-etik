from django.http import response
from django.shortcuts import redirect, render
from django.template.response import ContentNotRenderedError
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Transaksi

from keranjang.models import ItemKeranjang

# Create your views here.


def pembayaran(request):
    username = request.user.username
    item_not_available = validate_is_barang_available(username)
    if item_not_available:
        messages.error(request, "{} not available".format(", ".join(item_not_available)))
        return redirect('/keranjang/') 
    
    if request.method == 'POST':

        metode = request.POST.get('metode')

        lastTR = Transaksi.objects.last()

        if lastTR == None:
            newID = 'TR00001'

        else:
            lastID = int(lastTR.idTransaksi[2:])
            newID = lastID + 1

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
            usernamePembeli = username,
            caraPembayaran = metode,
            timeStamp = timezone.now(),
            totalPesanan = get_total_pesanan(username)
        )

        newTR.save()

        set_item_keranjang_tr(username, newTR)
        set_jumlah_barang_minus(username, newTR)
    
        return redirect('transaksi:transaksiChecker', id = newID)

    context = {}

    context['items'] = get_items(username)


    return render(request, 'pembayaran.html', context)


def transaksiChecker(request, id):

    TR = Transaksi.objects.get(idTransaksi = id)

    context = {'transaksi':TR}

    username = request.user.username

    context['items'] = get_items_by_tr(username, TR)


    if request.method == 'POST':
        
        action = request.POST.get('action')

        if action == 'konfirmasi':
            TR.statusTransaksi = 'menunggu konfirmasi admin'

            TR.save()


            return render(request, 'transaksi-konfirm.html', context)

        elif action == 'batal':
            set_jumlah_barang_plus(username, TR)

            TR.statusTransaksi = 'transaksi dibatalkan'

            TR.save()


            return render(request, 'transaksi-done.html', context)

    if request.method == 'GET':

        status = TR.statusTransaksi

        if status == 'menunggu konfirmasi pembayaran':
            return render(request, 'transaksi-bayar.html', context)

        elif status == 'menunggu konfirmasi admin':
            return render(request, 'transaksi-konfirm.html', context)

        else:
            return render(request, 'transaksi-done.html', context)

def transaksiViewer(request):
    context = {"transaksi":Transaksi.objects.all()}

    return render(request, 'transaksi-viewer.html', context)

def transaksiAdmin(request, id):
    TR = Transaksi.objects.get(idTransaksi = id)
    username = TR.usernamePembeli

    context = {"transaksi":TR}

    context['items'] = get_items_by_tr(username, TR)

    print(context)

    return render(request, 'transaksi-admin.html', context)


def validate_is_barang_available(username):
    item_keranjangs = ItemKeranjang.objects.filter(pelanggan__username = username, transaksi=None)
    item_not_available = []
    for item in item_keranjangs:
        jumlah_stok = item.barang.stok
        jumlah_permintaan = item.jumlah_item
        if jumlah_stok < jumlah_permintaan:
            item_not_available.append(item.barang.nama)

    return item_not_available

def get_items(username):
    context = []

    item_keranjang = ItemKeranjang.objects.filter(pelanggan__username = username,  transaksi=None)

    total_price = 0
    n = 0
    for item in item_keranjang:
        nama = item.barang.nama
        image_url = item.barang.image_url
        harga = item.barang.harga
        jumlah = item.jumlah_item
        total_price += jumlah * harga
        context.append([nama, harga, jumlah, image_url])
        n+=1

    context.append(['totalPesanan', total_price])


    return context

def get_items_by_tr(username, tr):
    context = []

    item_keranjang = ItemKeranjang.objects.filter(pelanggan__username = username,  transaksi=tr)

    total_price = 0
    n = 0
    for item in item_keranjang:
        nama = item.barang.nama
        image_url = item.barang.image_url
        harga = item.barang.harga
        jumlah = item.jumlah_item
        total_price += jumlah * harga
        context.append([nama, harga, jumlah, image_url])
        n+=1

    context.append(['totalPesanan', total_price])

    return context

def get_total_pesanan(username):
    item_keranjang = ItemKeranjang.objects.filter(pelanggan__username = username,  transaksi=None)

    total_price = 0
    for item in item_keranjang:
        harga = item.barang.harga
        jumlah = item.jumlah_item
        total_price += jumlah * harga

    return total_price

def set_item_keranjang_tr(username, tr):
    item_keranjang = ItemKeranjang.objects.filter(pelanggan__username = username, transaksi = None)

    for item in item_keranjang:
        item = ItemKeranjang.objects.get(pelanggan = item.pelanggan, barang = item.barang, transaksi = None)
        item.transaksi = tr
        item.save()

def set_jumlah_barang_minus(username, tr):
    item_keranjang = ItemKeranjang.objects.filter(pelanggan__username = username,  transaksi = tr)

    for item in item_keranjang:
        item = ItemKeranjang.objects.get(pelanggan = item.pelanggan, barang = item.barang, transaksi = tr)
        barang = item.barang
        barang.stok = barang.stok - item.jumlah_item
        barang.save()

def set_jumlah_barang_plus(username, tr):
    item_keranjang = ItemKeranjang.objects.filter(pelanggan__username = username, transaksi = tr)

    for item in item_keranjang:
        item = ItemKeranjang.objects.get(pelanggan = item.pelanggan, barang = item.barang, transaksi = tr)
        barang = item.barang
        barang.stok = barang.stok + item.jumlah_item
        barang.save()




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
