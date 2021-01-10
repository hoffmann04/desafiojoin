from django import forms
from .models import Alvo
from django.forms import ModelForm, DateInput

# Formulário usado para criar e editar um alvo
class AlvoForm(forms.ModelForm):
    class Meta:
        model = Alvo
        # datetime-local é um input type do HTML5, formato pra mostrar datetime no campo
        widgets = {
            'data_expiracao': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = ('nome', 'latitude', 'longitude', 'data_expiracao')

    def __init__(self, *args, **kwargs):
        super(AlvoForm, self).__init__(*args, **kwargs)
        # input_formats pra fazer o parser do datetime-local do HTML5 para um datetime field
        self.fields['data_expiracao'].input_formats = ('%Y-%m-%dT%H:%M',)