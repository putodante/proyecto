from django import forms
from apps.alumnos.models import Alumnos

class AlumnosForm(forms.ModelForm):
    class Meta:
        model= Alumnos

        fields = [
            'profesor',
            'nombre',
            'apellidos',
            'sexo',
            'edad',
            'fechaMatricula',
            'castigos',
        ]
        labels={
            'profesor': 'Profesor',
            'nombre': 'Nombre',
            'apellidos':'Apellidos',
            'sexo':'Sexo',
            'edad':'Edad',
            'fechaMatricula':"Fecha matriculación",
            'castigos':'Castigos',
        }
        widgets={
            'profesor':forms.Select(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.NumberInput(attrs={'class':'form-control'}),
            'fechaMatricula':forms.DateTimeInput(attrs={'class':'form-control'}),
            'castigos':forms.CheckboxSelectMultiple(),
        }