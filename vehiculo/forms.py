from django import forms
from .models import Vehiculo #Esto importa el modelo Vehiculo que has definido en models.py

#class VehiculoForm(forms.ModelForm): #clase llamada VehiculoForm que hereda de forms.ModelForm, que es una clase de Django que facilita la creación de formularios basados en modelos.
    #class Meta: #clase anidada dentro de VehiculoForm que permite especificar la configuración del formulario.
        #model = Vehiculo  #modelo utilizando para crear el formulario.
        #fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio'] # incluiye todos los campos del modelo en el formulario. También se puede especificar campos específicos como fields = ['marca', 'modelo']



class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
    
    # Opciones para el campo 'marca'
    MARCA_CHOICES = [
        ('Ford', 'Ford'),
        ('Chevrolet', 'Chevrolet'),
        ('Toyota', 'Toyota'),
    ]
    
    # Opciones para el campo 'categoria'
    CATEGORIA_CHOICES = [
        ('particular', 'Particular'),
        ('transporte', 'Transporte'),
        ('carga', 'Carga'),
    ]
    
    # Campos de tipo 'ChoiceField' que se renderizan como un <select>
    marca = forms.ChoiceField(choices=MARCA_CHOICES, label="Marca", widget=forms.Select)
    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES, label="Categoría", widget=forms.Select)
