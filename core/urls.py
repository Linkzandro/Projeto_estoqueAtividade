from django.urls import path
from core.views import Index,DetalhesProduto,ListarFornecedores,ListarCategorias,cadastrar_produtos

urlpatterns = [
    path('',Index,name='Index'),
    path('detalhes_produto/<int:produto_pk>',DetalhesProduto,name='detalhes_produto'),
    path('fornecedores',ListarFornecedores,name='fornecedores'),
    path('categorias',ListarCategorias,name='categorias'),
    path('cadastrar_produtos',cadastrar_produtos,name='cadastrar_produtos')
    
]