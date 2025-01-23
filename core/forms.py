from django import forms
from .models import Produto,Categoria

class ProdutoForm(forms.ModelForm):

    class Meta:
        model=Produto
        fields='__all__'
        exclude=['data_criacao']

    categoria=forms.ModelChoiceField(queryset=Categoria.objects.all(),widget=forms.CheckboxSelectMultiple())