from django.shortcuts import redirect, render
from admin_warung.models import Barang


def home(request):
    list_barang = Barang.objects.all()

    if request.method == 'POST':
        key = request.POST.get('search')
        print(request.POST.get('search'))
        return redirect('main:search', search = key)

    return render(request, 'main/home.html', {'list_barang':list_barang})

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def search(request, search):
    context = {}
    context['key'] = search

    list_barang = Barang.objects.filter(nama__icontains = search)

    context['list_barang'] = list_barang

    return render(request, 'main/search.html', context)