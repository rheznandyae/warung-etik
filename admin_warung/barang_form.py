from django import forms
from .models import Barang

class BarangForm(forms.Form):
    class Meta:
        model = Barang
        fields = "__all__"

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()