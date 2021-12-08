from django.http import response
from django.shortcuts import get_object_or_404, render
from admin_warung.models import Barang
from review.models import ReviewBarang
from keranjang.models import ItemKeranjang

def detail_barang(request, id):
    barang = get_object_or_404(Barang, id=id)
    user = request.user

    barangReviewsList = ReviewBarang.objects.filter(barang=barang)
    listItemKeranjangUser = ItemKeranjang.objects.filter(pelanggan=user, barang=barang)
    userBoughtItem = cekUserPernahBeliBarang(listItemKeranjangUser)
    alreadyWroteBool = cekUserPernahTulisReview(barangReviewsList, user)


    context = {
        "barang":barang,
        "alreadyWrote":alreadyWroteBool,
        "bought":userBoughtItem
    }
    return render(request, 'detail-barang.html', context)

def cekUserPernahBeliBarang(listItemKeranjang):
    userBoughtItem = False
    for item in listItemKeranjang:
        if(item.transaksi != None):
            if item.transaksi.statusTransaksi == "transaksi berhasil":
                userBoughtItem = True
    return userBoughtItem

def cekUserPernahTulisReview(barangReviewsList, user):
    alreadyWroteBool = False
    for review in barangReviewsList:
        if review.author == user:
            alreadyWroteBool = True
    return alreadyWroteBool
