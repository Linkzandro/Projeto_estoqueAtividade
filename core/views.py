from django.shortcuts import render
from .models import Produto,Fornecedor,Categoria

def Index(request):
    produtos=Produto.objects.all().order_by('-data_criacao')
    context={'itens':produtos}
    return render(request,'Index.html',context)


def ListarFornecedores(request):
    fornecedores=Fornecedor.objects.all()
    context={'itens':fornecedores}
    return render(request,'fornecedores.html',context)

def ListarCategorias(request):
    categorias=Categoria.objects.all()
    context={'itens':categorias}
    return render(request,'categorias.html',context)

def DetalhesProduto(request,produto_pk):
    item=Produto.objects.get(id=produto_pk)
    return render(request,'detalhes_produto.html',{'item':item})