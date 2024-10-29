from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'email', 'rol', 'departamento', 'telefono', 'fecha_contratacion']
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }