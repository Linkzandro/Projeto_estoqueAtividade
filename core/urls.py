from django.urls import path
from core.views import Index,DetalhesProduto,ListarFornecedores,ListarCategorias

urlpatterns = [
    path('',Index,name='Index'),
    path('detalhes_produto/<int:produto_pk>',DetalhesProduto,name='detalhes_produto'),
    path('fornecedores',ListarFornecedores,name='fornecedores'),
    path('categorias',ListarCategorias,name='categorias'),
    
]