from django import forms
from .models import Produto,Categoria,Fornecedor
import re
from django.core.exceptions import ValidationError

class ProdutoForm(forms.ModelForm):

    def clean_codigo(self):
        if not re.search("^[A-Za-z0-9_-]*$",self.cleaned_data.get('codigo')):
            raise ValidationError("codigo deve conter apenas letras e/ou números")
        return self.cleaned_data.get('codigo')
        
    def clean_preco(self):
        if self.cleaned_data.get('preco')<0:
            raise ValidationError("Preço deve ser maior que zero")
        return self.cleaned_data.get('preco')
        
    def clean_quantidade_estoque(self):
        if self.cleaned_data.get('quantidade_estoque')<0:
            raise ValidationError("estoque não deve ter um valor abaixo de zero")
        return self.cleaned_data.get('quantidade_estoque')
        
    def clean_nome(self):
        if len(self.cleaned_data.get('nome'))<3:
            raise ValidationError("o nome do produto deve ter pelo menos 3 caracteres")
        return self.cleaned_data.get('nome')
    
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
        
