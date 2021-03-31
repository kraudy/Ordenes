from django import forms
from .models import Orden

class OrdenForm(forms.Form):
    class Meta:
        model = Orden
        fields = '__all__'
        #exclude = ['foo']


