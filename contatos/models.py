from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    
    nome = models.CharField(max_length=255)
    
    # Adicionando o nome da categoria no Django admin
    def __str__(self) -> str:
        return self.nome
    
class Contato(models.Model):
    
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(max_length=255, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    
    # Adicionando o nome da categoria no Django admin
    def __str__(self) -> str:
        return self.nome