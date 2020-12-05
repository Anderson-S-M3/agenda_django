from django.shortcuts import render, get_object_or_404
from django.db.models.expressions import Value
from django.db.models.functions import Concat
from django.core.paginator import Paginator
from django.db.models.query_utils import Q
from django.http import Http404
from .models import Contato


def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        ocultar = True
    )
    paginator = Paginator(contatos, 1) # Show 25 contacts per page

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {"contatos": contatos})


def detalhe_contato(request, contato_id):
    contato = get_object_or_404(Contato, id = contato_id)

    if not contato.ocultar:
        raise Http404()

    return render(request, 'detalhes/detalhe.html', {'contato': contato})


def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome') 

    contatos = Contato.objects.annotate(
        nome_completo = campos
    ).filter(
        Q(nome_completo__icontains = termo) | Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 1) # Show 25 contacts per page

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {"contatos": contatos})
