from django.shortcuts import render
from admin_warung.models import Barang


def home(request):
    list_barang = Barang.objects.all()

    return render(request, 'main/home.html', {'list_barang':list_barang})

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def search(request):
    return render(request, 'main/search.html')