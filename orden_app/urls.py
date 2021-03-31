from django.urls import path, include
from . import views
from orden_app.views import OrdenListView

app_name = "orden_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', OrdenListView.as_view(), name='orden_lista'),
]


