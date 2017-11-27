from django import forms
from apps.profesores.models import profesores

class ProfesorForm(forms.ModelForm):
    class Meta:
        model=profesores

        fields=[
            'nombre',
            'apellidos',
            'edad',
            'email',
            'materia'
        ]
        labels={
            'nombre':'Nombre',
            'apellidos':'Apellidos',
            'edad':'Edad',
            'email':'E-mail',
            'materia':'Materia',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'materia':forms.Select(attrs={'class': 'form-control'})
        }
