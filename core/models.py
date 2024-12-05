from django.db import models
from datetime import datetime

# Create your models here.
class Produto(models.Model):
    nome=models.CharField(max_length=140)
    codigo=models.CharField(max_length=140,unique=True)
    desc=models.TextField(blank=True,null=True)
    preco=models.DecimalField(max_digits=18,decimal_places=2)
    quantidade_estoque=models.IntegerField()
    data_criacao=models.DateField(default=datetime.now)