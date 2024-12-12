from django.contrib import admin
from .models import Produto,Categoria,Fornecedor

class ProdutoAdmin(admin.ModelAdmin):
    list_display=['codigo','nome','preco','quantidade_estoque','data_criacao']
    search_fields=['codigo','nome']
    filter=['data_criacao']
    ordering=['-data_criacao']



admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(Fornecedor)