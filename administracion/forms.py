from django import forms
from .models import Animal, Cliente

# class AnimalForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", max_length=120)
#     raza = forms.CharField(label="Raza", max_length=120)
#     categoria = forms.CharField(label="Categoria", max_length=120)
#     dueno = forms.IntegerField(label="Dueño")




# class ClienteForm(forms.Form):
#     num_dni = forms.IntegerField(label="DNI")
#     nombre = forms.CharField(label="Nombre", max_length=120)
#     apellido = forms.CharField(label="Apellido", max_length=120)
#     direccion = forms.CharField(label="Direccion", max_length=120)

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            "dni": forms.NumberInput(attrs={
                "class": "form-control"
            }),
            "nombre": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "apellido": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "direccion": forms.TextInput(attrs={
                "class": "form-control"
            }), 
        }