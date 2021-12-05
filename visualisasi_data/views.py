from django.http import response
from django.shortcuts import render
from django.views.generic import TemplateView
#from .models import Transaksi
from transaksi.models import Transaksi
from keranjang.models import ItemKeranjang
from admin_warung.models import Barang

class TransaksiChartView(TemplateView):
    template_name = 'data-vis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transaksi"] = Transaksi.objects.all()
        context["barang"] = Barang.objects.all()
        context["item_keranjang"] = ItemKeranjang.objects.all()
        return context