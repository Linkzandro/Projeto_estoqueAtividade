from django.shortcuts import render
from .models import Produto

def Index(request):
    produtos=Produto.objects.all().order_by('-data_criacao')
    context={'itens':produtos}
    return render(request,'Index.html',context)