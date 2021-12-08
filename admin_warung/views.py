from django.http import response, HttpResponseNotAllowed
from .barang_form import BarangForm, ExcelUploadForm
from django.shortcuts import redirect, render

from transaksi.models import Transaksi

def dashboard(request):

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'konfirmasi':
            idTransaksi = request.POST.get('transaksi')
            update_transaksi(idTransaksi)

            redirect('admin_warung:dashboard')
        else:
            idTransaksi = request.POST.get('transaksi')
            update_status(idTransaksi)

            redirect('admin_warung:dashboard')

    context = {
        "excel_upload_form": ExcelUploadForm(),
    }

    context['transaksi'] = get_all_transaksi()

    # print(context)
    return render(request, 'dashboard.html', context=context)

def detail_barang_admin_view(request):
    response = {}
    return render(request, 'detail_barang_admin.html', response)


def hapus_barang_view(request):
    response = {}
    return render(request, 'hapus_barang.html', response)


def tambah_barang_view(request):
    response = {}
    response['error'] = False
    form = BarangForm(request.POST or None)
    response['form'] = form
    if(request.method == 'POST' and form.is_valid()):
        nama = request.POST['nama']
        stok = request.POST['stok']
        terjual = request.POST['terjual']
        deskripsi = request.POST['deskripsi']
        gambar = request.POST['gambar']
    
    return render(request, 'tambah_barang.html', response)


def ubah_barang_view(request):
    response = {}
    response['error'] = False
    form = BarangForm(request.POST or None)
    response['form'] = form
    if(request.method == 'POST' and form.is_valid()):
        nama = request.POST['nama']
        stok = request.POST['stok']
        terjual = request.POST['terjual']
        deskripsi = request.POST['deskripsi']
        gambar = request.POST['gambar']

    return render(request, 'ubah_barang.html', response)


def list_ubah_view(request):
    response = {}
    return render(request, 'list_ubah.html', response)

def list_hapus_view(request):
    response = {}
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

def update_status(id):
    context = []

    transaksi = Transaksi.objects.get(idTransaksi = id)

    transaksi.statusTransaksi = 'menunggu konfirmasi pembayaran'

    transaksi.save()

    return context