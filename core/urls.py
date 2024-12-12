from django.urls import path
from core.views import Index,DetalhesProduto

urlpatterns = [
    path('',Index,name='index'),
    path('detalhes_produto/<int:produto_pk>',DetalhesProduto,name='detalhes_produto')
    
]