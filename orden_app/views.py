from django.shortcuts import render


def index(request):
    return render(request, 'orden_app/index.html', {})


