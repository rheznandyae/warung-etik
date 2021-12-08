from django.http import response
from django.shortcuts import redirect, render
from admin_warung.models import Barang
from .models import ReviewBarang

def tulis(request, id):
    barang = Barang.objects.get(id=id)
    context = {
        'barang':barang
    }
    if request.method == "POST":
        barang = Barang.objects.get(id=id)
        bintang = request.POST.get("rate")
        content = request.POST.get("content")

        review = ReviewBarang.objects.create(barang=barang, bintang=bintang, content=content)
        redir = f'/barang/detail/{id}/#ulasan'
        return redirect(redir)


    return render(request, 'tulis-review.html', context=context)

def edit(request, id):
    review = ReviewBarang.objects.get(id=id)
    context = {
        "review":review
    }
    if request.method == "POST":
        barang = Barang.objects.get(id=id)
        bintang = request.POST.get("rate")
        content = request.POST.get("content")

        review = ReviewBarang.objects.update(id=id, barang=barang, bintang=bintang, content=content)
        redir = f'/barang/detail/{id}/#ulasan'
        return redirect(redir)
    return render(request, 'edit-review.html', context=context)