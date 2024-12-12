from django.shortcuts import render
from .models import Produto

def Index(request):
    produtos=Produto.objects.all().order_by('-data_criacao')
    context={'itens':produtos}
    return render(request,'Index.html',context)

def DetalhesProduto(request,produto_pk):
    item=Produto.objects.get(id=produto_pk)
    return render(request,'detalhes_produto.html',{'item':item})