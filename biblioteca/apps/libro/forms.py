from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        

# CRUD CON PYTHON PURO Y VISTAS BASADAS EN FUNCIONES