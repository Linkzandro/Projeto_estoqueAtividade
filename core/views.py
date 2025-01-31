from django.shortcuts import render,redirect
from .models import Produto,Fornecedor,Categoria
from .forms import ProdutoForm,CategoriaForm,FornecedorForm

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
        
        form=ProdutoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('Index')
    return render(request,'core/cadastrar_produtos.html',{'form':form})

def excluir_produto(request,produto_pk):
    produto=Produto.objects.get(id=produto_pk)
    produto.delete()
    return redirect('Index')

def cadastrar_categorias(request):
    if request.method=='POST':
        
        form=CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Index')
    form=CategoriaForm()
    return render(request,'core/cadastrar_categoria.html',{'form':form})

def excluir_categorias(request,categorias_pk):
    produto=Categoria.objects.get(id=categorias_pk)
    produto.delete()
    return redirect('Index')

def cadastrar_fornecedores(request):
    if request.method=='POST':
        
        form=FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Index')
    form=FornecedorForm()
    return render(request,'core/cadastrar_fornecedor.html',{'form':form})

def excluir_fornecedores(request,fornecedores_pk):
    produto=Fornecedor.objects.get(id=fornecedores_pk)
    produto.delete()
    return redirect('Index')