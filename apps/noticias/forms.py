from django import forms
from apps.noticias.models import noticias

class noticiaform(forms.ModelForm):
   class Meta:
        model=noticias
        fields=[
            'Titulo',
            'Cuerpo',
            'Logo'
        ]
        labels={
            'Titulo': 'Titulo',
            'Cuerpo':'Cuerpo',
            'Logo':'Logo',
        }
        widgets={
        'Titulo': forms.TextInput(attrs={'class':'form-control'}),
        'Cuerpo': forms.Textarea(attrs={'class':'form-control'}),

        }

