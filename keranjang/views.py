from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from admin_warung.models import Barang
from keranjang.serializers import ItemKeranjangSerializers
from .models import ItemKeranjang
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User

def keranjang_view(request):
    context={
        'list_barang':[
            {
                'nama': 'Mie Goreng',
                'keterangan': 'Mie instant enak',
                'jumlah_item': '20',
                'image':'https://images.unsplash.com/photo-1638518945531-ff6290869fb2'
            },
            {
                'nama': 'Mie Goreng',
                'keterangan': 'Mie instant enak',
                'jumlah_item': '20',
                'image':'https://images.unsplash.com/photo-1638518945531-ff6290869fb2'
            }
        ]
    }

    return render(request, 'keranjang.html', context=context)

@api_view(['GET'])
def get_item_keranjang_by_user(request, username):
    item_keranjangs = ItemKeranjang.objects.filter(pelanggan__username = username, transaksi=None)
    item_serializer = ItemKeranjangSerializers(instance=item_keranjangs, many=True)
    return Response(item_serializer.data)

@api_view(["POST"])
def create_item_keranjang(request):
    username = request.data['username']
    id_barang = request.data['id_barang']
    jumlah_item = request.data['jumlah_item']
    print(request.POST['jumlah_item'])
    item_keranjang = ItemKeranjang.objects.filter(pelanggan__username = username, barang__id = id_barang, transaksi=None)
    if not item_keranjang.exists() :
        new_item_keranjang = ItemKeranjang(
            pelanggan = User.objects.get(username=username),
            barang = Barang.objects.get(id=id_barang),
            jumlah_item = jumlah_item
            )
        new_item_keranjang.save()
    else:
        print("udah ada dude")
    return Response(request.data)
    
@api_view(['POST'])
def plus1_amount_item_keranjang(request):
    id_keranjang = request.data['id_keranjang']
    item_keranjang = ItemKeranjang.objects.get(id = id_keranjang)

    item_keranjang.jumlah_item += 1
    item_keranjang.save()
    item_serializer = ItemKeranjangSerializers(instance=item_keranjang)

    return Response(item_serializer.data)

@api_view(['POST'])
def minus1_amount_item_keranjang(request):
    id_keranjang = request.data['id_keranjang']

    item_keranjang = ItemKeranjang.objects.get(id = id_keranjang)

    item_keranjang.jumlah_item -= 1
    
    if item_keranjang.jumlah_item > 0 :
        item_keranjang.save()
    else :
        ItemKeranjang.objects.get(id = item_keranjang.id).delete()
    item_serializer = ItemKeranjangSerializers(instance=item_keranjang)

    return Response(item_serializer.data)

@api_view(['GET','DELETE'])
def item_keranjang_detail(request, id_keranjang):

    if request.method == 'GET':
        item_keranjang = ItemKeranjang.objects.get(id = id_keranjang)
        item_serializer = ItemKeranjangSerializers(instance=item_keranjang)

        return Response(item_serializer.data)

    if request.method == 'DELETE':
    # id_keranjang = request.data['id_keranjang']
        ItemKeranjang.objects.filter(id = id_keranjang).delete()
        return Response({"message": "delete item {}".format(id_keranjang)})

@api_view(['GET'])
def get_total_price(request,username):
    item_keranjangs = ItemKeranjang.objects.filter(pelanggan__username = username,  transaksi=None)

    total_item = 0
    total_price = 0
    for item in item_keranjangs:
        total_item += 1
        total_price += item.jumlah_item * item.barang.harga

    return Response({
        'total_price' : total_price,
        'total_item' : total_item
        })














