from django.http import response, HttpResponseNotAllowed
from .barang_form import BarangForm, ExcelUploadForm
from django.shortcuts import render



def dashboard(request):
    context = {
        "excel_upload_form": ExcelUploadForm(),
    }
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