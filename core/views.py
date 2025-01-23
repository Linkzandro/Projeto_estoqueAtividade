from django.shortcuts import render,redirect
from .models import Produto,Fornecedor,Categoria
from .forms import ProdutoForm

def Index(request):
    produtos=Produto.objects.all().order_by('-data_criacao')
    context={'itens':produtos}
    return render(request,'core/Index.html',context)


def ListarFornecedores(request):
    fornecedores=Fornecedor.objects.all()
    context={'itens':fornecedores}
    return render(request,'core/fornecedores.html',context)

def ListarCategorias(request):
    categorias=Categoria.objects.all()
    context={'itens':categorias}
    return render(request,'core/categorias.html',context)

def DetalhesProduto(request,produto_pk):
    item=Produto.objects.get(id=produto_pk)
    return render(request,'core/detalhes_produto.html',{'item':item})

def cadastrar_produtos(request):
    if request.method=='POST':
        form=ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Index')
    form=ProdutoForm()
    return render(request,'core/cadastrar_produtos.html',{'form':form})