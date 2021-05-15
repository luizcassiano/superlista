from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

PRIORIDADE = [(1, 'ALTA'),
              (2, 'MEDIA'),
              (3, 'ALTA')]


class ListaPrioridade(forms.Form):
    ds_list = forms.CharField(max_length=200)
    ds_prioridade = favorite_fruit = forms.CharField(label='Qual a prioridade desse item?',
                                                     widget=forms.RadioSelect(choices=PRIORIDADE))


