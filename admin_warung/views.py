from os import name
from django.http import response, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Barang
from .barang_form import BarangForm, ExcelUploadForm

from openpyxl import load_workbook, Workbook
from openpyxl.utils import get_column_letter
from openpyxl.utils.datetime import to_excel
from openpyxl.writer.excel import save_virtual_workbook
from openpyxl.styles import Border, Side, Alignment, PatternFill

import copy
from datetime import datetime

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

# def import_barang(request):
#     if request.method == "GET":
#         context = {
#             "excel_upload_form": ExcelUploadForm(),
#         }
#         return render(request, 'dashboard.html',)

#     if request.method == "POST":
#         context = {"excel_upload_form": ExcelUploadForm()}
#         return render(request, 'dashboard.html',)

#     return HttpResponseNotAllowed(["GET", "POST"])


def import_barang(request):
    form = ExcelUploadForm(request.POST, request.FILES)
    if form.is_valid():
        workbook = load_workbook(request.FILES["excel_file"])
        sheet = workbook.active
        Barang.objects.all().delete()   
        
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if(row[0] == None):
                break
            barang = Barang(nama=row[1],
                            harga=row[2],
                            stok=row[3],
                            terjual=row[4],
                            deskripsi=row[5],
                            image_url=row[6])

            barang.save()
            
        return redirect(reverse_lazy('admin_warung:dashboard'))
    

def export_barang():
    wb = Workbook()

    ws = wb.active
    ws.title = "Barang"
    
    # Creating column header
    title_list = ['No.', 'Nama', 'Harga', 'Stok', 'Terjual', 'Deskripsi', 'Image URL']
    ws.append(title_list)
    
    # Data insertion
    all_barang = Barang.objects.all().order_by('id')
    num_of_data = len(all_barang)
    
    for barang in all_barang:
        ws.append(barang.get_all_value())
        

    ### Styling ###
    
    # Column Size
    ws.column_dimensions['A'].width = 6
    for col in range(2, 8):
        ws.column_dimensions[get_column_letter(col)].width = 25
        if col == 6:
            ws.column_dimensions[get_column_letter(col)].width = 50
    
    # Row Size
    ws.row_dimensions[1].height = 40

    for row in range(2, num_of_data + 2):
        ws.row_dimensions[row].height = 60

    # Coloring & format
    
    for row in range(1, num_of_data + 2):
        for col in range(1, 8):
            ws["{}{}".format(get_column_letter(col), row)].alignment = Alignment(
                horizontal="center", vertical="center")

            ws[f'{get_column_letter(col)}{row}'].border = Border(left=Side(border_style="thin",
                                                                            color='00000000'),
                                                                  right=Side(border_style="thin",
                                                                             color='00000000'),
                                                                  top=Side(border_style="thin",
                                                                           color='00000000'),
                                                                  bottom=Side(border_style="thin",
                                                                              color='00000000'),
                                                                  )
            if(row == 1):
                ws[f'{get_column_letter(col)}{row}'].fill = PatternFill( "solid", fgColor="0B3C5C")
                
    for row in ws.iter_rows():
        for cell in row:
            alignment = copy.copy(cell.alignment)
            alignment.wrapText = True
            cell.alignment = alignment

    return wb

def download(_):
    response = HttpResponse(save_virtual_workbook(
        export_barang()), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="Export_Barang-{datetime.now()}.xlsx"'
    return response



    
