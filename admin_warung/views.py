from django.http import response, HttpResponseNotAllowed
from .models import *
from admin_warung.models import Barang
from .barang_form import BarangForm, ExcelUploadForm
from django.shortcuts import redirect, render, get_object_or_404


from transaksi.models import Transaksi

def dashboard(request):
    barangs = Barang.objects.all()

    if request.method == 'POST':
        idTransaksi = request.POST.get('transaksi')
        update_transaksi(idTransaksi)

        redirect('admin_warung:dashboard')

    context = {
        "excel_upload_form": ExcelUploadForm(),
        "barangs": barangs,
    }

    context['transaksi'] = get_all_transaksi()

    # print(context)
    return render(request, 'dashboard.html', context=context)

def detail_barang_admin_view(request, id):
    response = {}
    barang = get_object_or_404(Barang, id=id)
    response['barang'] = barang

    return render(request, 'detail_barang_admin.html', response)


def hapus_barang_view(request, id):
    response = {}
    barang = get_object_or_404(Barang, id=id)
    response['barang'] = barang

    if(request.method == 'POST'):
        barang.delete()

        return redirect('/dashboard')

    return render(request, 'hapus_barang.html', response)


def tambah_barang_view(request):
    response = {}
    if(request.method == 'POST'):
        nama = request.POST.get("nama")
        harga = request.POST.get("harga")
        stok = request.POST.get("stok")
        terjual = request.POST.get("terjual")
        deskripsi = request.POST.get("deskripsi")
        image_url = request.POST.get("image_url")

        barang = Barang.objects.create(nama=nama, harga=harga, stok=stok, terjual=terjual, deskripsi=deskripsi, image_url=image_url)
        redir = f'/dashboard/detail-barang/{barang.id}'
        return redirect(redir)
    
    return render(request, 'tambah_barang.html', response)


def ubah_barang_view(request, id):
    response = {}
    barang = get_object_or_404(Barang, id=id)
    response['barang'] = barang

    if(request.method == 'POST'):
        nama = request.POST.get("nama")
        harga = request.POST.get("harga")
        stok = request.POST.get("stok")
        terjual = request.POST.get("terjual")
        deskripsi = request.POST.get("deskripsi")
        image_url = request.POST.get("image_url")

        Barang.objects.filter(id=id).update(nama=nama, harga=harga, stok=stok, terjual=terjual, deskripsi=deskripsi, image_url=image_url)
        redir = f'/dashboard/detail-barang/{id}'
        return redirect(redir)

    return render(request, 'ubah_barang.html', response)


def list_ubah_view(request):
    response = {}
    barangs = Barang.objects.all()
    response['barangs'] = barangs
    return render(request, 'list_ubah.html', response)

def list_hapus_view(request):
    response = {}
    barangs = Barang.objects.all()
    response['barangs'] = barangs
    return render(request, 'list_hapus.html', response)

def import_barang(request):
    if request.method == "GET":
        context = {
            "excel_upload_form": ExcelUploadForm(),
        }
        return render(request, 'dashboard.html',)

    if request.method == "POST":
        context = {"excel_upload_form": ExcelUploadForm()}
        return render(request, 'dashboard.html',)

    return HttpResponseNotAllowed(["GET", "POST"])



def get_all_transaksi():
    context = []

    transaksi = Transaksi.objects.all()

    for tr in transaksi:
        id = tr.idTransaksi
        date = tr.timeStamp
        pembeli = tr.usernamePembeli
        total = tr.totalPesanan
        cara = tr.caraPembayaran
        status = tr.statusTransaksi
        context.append([id, date, pembeli, total, cara, status])

    return context

def update_transaksi(id):
    context = []

    transaksi = Transaksi.objects.get(idTransaksi = id)

    transaksi.statusTransaksi = 'transaksi berhasil'

    transaksi.save()

    return context