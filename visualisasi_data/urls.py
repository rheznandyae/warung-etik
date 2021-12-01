from django.urls import path

from . import views
from .views import TransaksiChartView

app_name = 'visualisasi_data'

urlpatterns = [
    path('', TransaksiChartView.as_view(), name='visualisasi'),
]
