from django import forms
from django.core.exceptions import ValidationError


PRIORIDADE = [(1, 'ALTA'),
              (2, 'MEDIA'),
              (3, 'ALTA')]


class ListaForms(forms.Form):
    ds_list = forms.CharField(label='Item',max_length=200)
    ds_prioridade = forms.ChoiceField(label='Prioridade', choices=PRIORIDADE, widget=forms.RadioSelect)

