from django import forms
from .models import Produto,Categoria,Fornecedor

class ProdutoForm(forms.ModelForm):

    class Meta:
        model=Produto
        fields='__all__'
        exclude=['data_criacao']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields='__all__'
        

class FornecedorForm(forms.ModelForm):
    class Meta:
        model=Fornecedor
        fields='__all__'
        
