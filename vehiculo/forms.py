from django import forms
from .models import Vehiculo, Marca

class VehiculoForm(forms.ModelForm):
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), label="Marca")


    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga')
    ]
    
    categoria = forms.ChoiceField(choices=CATEGORIAS, initial='Particular', label='Categoría')
    

    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_carroceria': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_motor': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }