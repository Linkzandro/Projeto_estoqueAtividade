from django.urls import path
from core.views import Index,DetalhesProduto,ListarFornecedores,ListarCategorias,cadastrar_produtos,excluir_produto,cadastrar_categorias,excluir_categorias,excluir_fornecedores,cadastrar_fornecedores

urlpatterns = [
    path('',Index.as_view(),name='Index'),
    path('detalhes_produto/<int:produto_pk>',DetalhesProduto.as_view(),name='detalhes_produto'),
    path('fornecedores',ListarFornecedores.as_view(),name='fornecedores'),
    path('categorias',ListarCategorias.as_view(),name='categorias'),
    path('cadastrar_produtos',cadastrar_produtos,name='cadastrar_produtos'),
    path('excluir_produtos/<int:produto_pk>',excluir_produto,name='excluir_produto'),
    path('cadastrar_categorias',cadastrar_categorias,name='cadastrar_categorias'),
    path('excluir_categorias/<int:categorias_pk>',excluir_categorias,name='excluir_categorias'),
    path('cadastrar_fornecedores',cadastrar_fornecedores,name='cadastrar_fornecedores'),
    path('excluir_fornecedores/<int:fornecedores_pk>',excluir_fornecedores,name='excluir_fornecedores'),

    
]