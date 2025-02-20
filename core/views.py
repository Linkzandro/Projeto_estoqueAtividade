from django.shortcuts import render,redirect
from .models import Produto,Fornecedor,Categoria
from .forms import ProdutoForm,CategoriaForm,FornecedorForm
from django.views.generic import ListView,DetailView

class Index(ListView):
    model=Produto
    template_name='core/Index.html' 
    context_object_name='itens'


class ListarFornecedores(ListView):
    model=Fornecedor
    template_name='core/fornecedores.html' 
    context_object_name='itens'


class ListarCategorias(ListView):
    model=Categoria
    template_name='core/categorias.html' 
    context_object_name='itens'

class DetalhesProduto(DetailView):
    pk_url_kwarg='produto_pk'
    model=Produto
    context_object_name='item'
    template_name='core/detalhes_produto.html'

def cadastrar_produtos(request):
    form=ProdutoForm()
    if request.method=='POST':
        form=ProdutoForm(request.POST or None,request.FILES)
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