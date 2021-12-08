from django.db.models.expressions import F
from django.http import response
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Count
from transaksi.models import Transaksi
from keranjang.models import ItemKeranjang
from admin_warung.models import Barang

class TransaksiChartView(TemplateView):
    template_name = 'data-vis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_transaksi = Transaksi.objects.all()
        list_barang = Barang.objects.all()
        list_item_keranjang = ItemKeranjang.objects.all()
        list_barang_with_income = Barang.objects.annotate(income=F('terjual') * F('harga'))

        print(list_barang_with_income)


        pemasukan = getTotalPemasukan(list_barang)
        
        transaksi_group_by_cara_pembayaran = Transaksi.objects.values('caraPembayaran').order_by('caraPembayaran').annotate(count=Count('caraPembayaran'))
        transaksi_group_by_status = Transaksi.objects.values('statusTransaksi').order_by('statusTransaksi').annotate(count_status=Count('statusTransaksi'))
        context["status_transaksi"] = transaksi_group_by_status
        context["cara_pembayaran"] = transaksi_group_by_cara_pembayaran
        context["transaksi"] = list_transaksi
        context["barang"] = list_barang
        context["item_keranjang"] = list_item_keranjang
        context["pemasukan"] = pemasukan
        context["income"] = list_barang_with_income
        return context

def getTotalPemasukan(list_barang):
    sum = 0
    for barang in list_barang:
        sum += (barang.harga * barang.terjual)
    return sum 