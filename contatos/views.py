from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models.expressions import Value
from django.db.models.functions import Concat
from django.core.paginator import Paginator
from django.db.models.query_utils import Q
from contatos.forms import ContatoForm
from django.contrib import messages
from django.http import Http404
from .models import Contato


@login_required(redirect_field_name='login')
def index(request):
    usuario = request.user

    contatos = Contato.objects.order_by('-id').filter(
        usuario=usuario,
        mostrar=True,
    )
    paginator = Paginator(contatos, 1)  # Show 25 contacts per page
    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {"contatos": contatos})


def detalhe_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'detalhes/detalhe.html', {'contato': contato})


def busca(request):
    usuario = request.user

    try:
        #Pesquisar
        termo = request.GET.get('termo')
        campos = Concat('nome', Value(' '), 'sobrenome')
        contatos = Contato.objects.annotate(
            nome_completo=campos
        ).filter(
            Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
        )
        #Mostrar resultado
        if termo == '':
            contatos = Contato.objects.order_by('-id').filter(
                usuario=usuario,
                mostrar=True,
            )
        if len(contatos) == 1:
            messages.info(request, f'{len(contatos)} contato encontrado')

        elif termo != '' and len(contatos) != 1:
            messages.info(request, f'{len(contatos)} contatos encontrados')

        paginator = Paginator(contatos, 1)  # Mostra 1 contato por pagina
        page = request.GET.get('page')
        contatos = paginator.get_page(page)

        return render(request, 'contatos/index.html', {"contatos": contatos})

    except ValueError:
        return redirect('/busca/?termo=')


@login_required(redirect_field_name='login')
def criar_contato(request):
    if not request.method == 'POST':
        form = ContatoForm()
        return render(request, 'contatos/add_contato.html', {'form':form})

    form = ContatoForm(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Formulario invalido')
        form = ContatoForm(request.POST)
        return render(request, 'contatos/add_contato.html', {'form':form})

    if not request.POST.get('nome') or not request.POST.get('telefone') or not request.POST.get('categoria'):
        messages.error(request, 'Preencha todos os campos obrigatorios')
        form = ContatoForm(request.POST)
        return render(request, 'contatos/add_contato.html', {'form':form})

    print(request.FILES)
    a = form.save(commit=False)
    a.usuario = request.user
    a.save()

    messages.success(request, 'Contato Criado com sucesso')
    return redirect('index_contatos')


