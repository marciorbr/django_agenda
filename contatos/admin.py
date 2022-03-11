from re import search
from django.contrib import admin
from .models import Categoria, Contato

# Class para adicionar campos na vizualização na página admin do Django
class ContatoAdmin(admin.ModelAdmin):
    
    list_display = ('id','nome', 'sobrenome', 'email', 'telefone', 'categoria', 'exibir')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'exibir')

# Adicionando Models ao django admin
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)