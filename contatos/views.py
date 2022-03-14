from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contato
from django.db.models import Q, Value
from django.db.models.functions import Concat

from django.contrib import messages

def index(request):
    
    contatos = Contato.objects.order_by('nome').filter(
        exibir = True
    )
    
    paginator = Paginator(contatos, 10) # Mostra 10 contatos por página
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
    
def ver_contato(request, contato_id):
    
    contato = get_object_or_404(Contato, id=contato_id)
    
    if not contato.exibir:
        raise Http404()
    
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
    
def busca(request):
    
    termo = request.GET.get('termo')
    
    campos = Concat('nome', Value(' '), 'sobrenome')
    
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo)
    )
    
    paginator = Paginator(contatos, 10) # Mostra 10 contatos por página
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })