from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Proceso, Orden, Ordenes_procesos

def index(request):
    return render(request, 'orden_app/index.html', {})

class OrdenListView(ListView):
    model = Orden

