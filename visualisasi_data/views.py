from django.http import response
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Transaksi

class TransaksiChartView(TemplateView):
    template_name = 'data-vis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Transaksi.objects.all()
        return context