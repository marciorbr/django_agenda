from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contato

def index(request):
    
    contatos = Contato.objects.all()
    
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