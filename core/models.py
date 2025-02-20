from django.db import models
from datetime import datetime

class Categoria(models.Model):
    nome=models.CharField(max_length=200)
    setor=models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.nome

class Fornecedor(models.Model):
    nome_fornecedor=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    
    def __str__(self) -> str:
        return self.nome_fornecedor

class Produto(models.Model):
    nome=models.CharField(max_length=140)
    codigo=models.CharField(max_length=140,unique=True)
    desc=models.TextField(blank=True,null=True)
    preco=models.DecimalField(max_digits=18,decimal_places=2)
    quantidade_estoque=models.IntegerField()
    data_criacao=models.DateField(default=datetime.now)
    foto=models.ImageField(null=True, blank=True, upload_to='produtos')


    fornecedor=models.ForeignKey(Fornecedor,on_delete=models.CASCADE,blank=True,null=True)
    categoria=models.ManyToManyField(Categoria)

    def __str__(self) -> str:
        return self.nome