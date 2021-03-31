from django.shortcuts import render

from .models import Proceso, Orden, Ordenes_procesos

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def index(request):
    return render(request, 'orden_app/index.html', {})

class OrdenListView(ListView):
    model = Orden

class OrdenDetailView(DetailView):
    model = Orden

class ProcesoListView(ListView):
    model = Proceso


