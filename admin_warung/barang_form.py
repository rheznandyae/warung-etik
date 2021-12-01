from django import forms

class BarangForm(forms.Form):
    nama = forms.CharField(label='Nama Barang', max_length=100)
    stok = forms.IntegerField(label='Jumlah Stok')
    terjual = forms.IntegerField(label='Terjual')
    deskripsi = forms.CharField(label='Deskripsi Barang', max_length=300)
    gambar = forms.ImageField(label='Gambar')

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()