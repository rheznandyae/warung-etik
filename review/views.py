from django.http import response
from django.shortcuts import redirect, render
from admin_warung.models import Barang
from .models import ReviewBarang

def tulis(request, id):
    
    context = {
        'id_barang':id
    }
    if request.method == "POST":
        barang = Barang.objects.get(id=id)
        bintang = request.POST.get("rate")
        content = request.POST.get("content")

        review = ReviewBarang.objects.create(barang=barang, bintang=bintang, content=content)
        redir = f'/barang/detail/{id}/#ulasan'
        return redirect(redir)


    return render(request, 'tulis-review.html', context=context)
