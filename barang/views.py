from django.http import response
from django.shortcuts import get_object_or_404, render
from admin_warung.models import Barang
from review.models import ReviewBarang

def detail_barang(request, id):
    barang = get_object_or_404(Barang, id=id)

    
    barangReviewsList = ReviewBarang.objects.filter(barang=barang)
    alreadyWroteBool = False
    for review in barangReviewsList:
        print(review)
        if review.author == request.user:
            print(review.author)
            alreadyWroteBool = True

    context = {
        "barang":barang,
        "alreadyWrote":alreadyWroteBool
    }
    return render(request, 'detail-barang.html', context)
