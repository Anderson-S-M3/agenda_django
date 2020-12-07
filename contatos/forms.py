from django.forms.fields import ImageField
from contatos.models import Categoria
from django import forms

class NameForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=50, required=True)
    sobrenome = forms.CharField(label='sobrenome', max_length=50, required=False)
    telefone = forms.CharField(label='telefone', max_length=20, required=True)

    descricao = forms.CharField(label='descricao', max_length=150, required=False)
    categoria = forms.ChoiceField(label='categoria', choices=[Categoria], required=True)

    foto = forms.ImageField()
