from django.shortcuts import render

from .models import Proceso, Orden, Ordenes_procesos

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

def index(request):
    return render(request, 'orden_app/index.html', {})

class OrdenListView(ListView):
    model = Orden

class OrdenDetailView(DetailView):
    model = Orden
    context_object_name = "orden_detalle"

class OrdenCreate(CreateView):
    model = Orden
    fields = ['nombre']

class ProcesoListView(ListView):
    model = Proceso

class ProcesoDetailView(DetailView):
    model = Proceso
    context_object_name = "proceso_detalle"


