from django import forms
from app.models import Proveedor

class FormularioProveedor(forms.ModelForm):
    class Meta: 
        model = Proveedor
        fields = "__all__"
        
