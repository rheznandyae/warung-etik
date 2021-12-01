from django.http import response
from django.shortcuts import render

def keranjang_view(request):
    context = {
        "list_barang":[
            {
                "nama" : "Indomie Rebus Ayam Bawang",
                "keterangan" : "Mie Instant This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.",
                "jumlah_item" : 4,
                "image": "https://warungmitra.com/wp-content/uploads/2021/02/indomie-ayam-bwg.jpg"
            },
            {
                "nama" : "Indomie Goreng Rendang",
                "keterangan" : "Mie Instant This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.",
                "jumlah_item" : 3,
                "image": "https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full//83/MTA-2902004/indomie_indomie-mie-goreng-rasa-rendang-91gr_full02.jpg"
            },
            {
                "nama" : "Ferrero Rocher",
                "keterangan" : "Snack Coklat This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.",
                "jumlah_item" : 6,
                "image" : "https://id-test-11.slatic.net/p/5a18bd1fa94e46269f63c44e66c20ac7.jpg"
            }
        ] 
    }
    return render(request, 'keranjang.html', context=context)

# Create your views here.
