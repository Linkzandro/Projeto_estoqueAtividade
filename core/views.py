
from django.shortcuts import render,redirect
from .models import Produto,Fornecedor,Categoria
from .forms import ProdutoForm,CategoriaForm,FornecedorForm,PesquisaForm
from django.views.generic import ListView,DetailView,FormView

class Index(ListView):
    model=Produto
    template_name='core/Index.html' 
    context_object_name='itens'
    paginate_by=5

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['navForm']=PesquisaForm()
        return context
    
    def get_queryset(self) :
        
        navform=PesquisaForm(self.request.GET or None)
        queryset=Produto.objects.all()

        if navform.is_valid():

            if navform.cleaned_data.get('pesquisa').strip()!='':
                queryset=queryset.filter(nome__icontains=navform.cleaned_data.get('pesquisa'))
            if navform.cleaned_data.get('maximo') and navform.cleaned_data.get('minimo'):
                queryset=queryset.filter(preco__range=(navform.cleaned_data.get('minimo'),navform.cleaned_data.get('maximo')))
                return queryset
            
            if navform.cleaned_data.get('minimo'):
                queryset=queryset.filter(preco__gte=navform.cleaned_data.get('minimo'))
                return queryset

            if navform.cleaned_data.get('maximo'):
                queryset=queryset.filter(preco__lte=navform.cleaned_data.get('maximo'))

        queryset=queryset.order_by('-id')
        return queryset
        

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
    if request.method=='POST':
        
        form=ProdutoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('Index')
    form=ProdutoForm()
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