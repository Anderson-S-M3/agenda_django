<h1 align="center">
<a href="https://github.com/Anderson-S-M3/agenda_django">🔗 Agenda Django</a>
</h1>

<p align="center">Agenda com funçoes de <b>Login, Crud, Research field</b>.</p>

<p align="center">
<img alt="skill-python" src="https://img.shields.io/badge/Python-3776AB?style=badge&logo=python&logoColor=white"> <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen"> <img alt="PyPI - Django Version badge" src="https://img.shields.io/badge/django%20versions-2.2.16-blue">
</p>

<h5 align="center"> 🚧 Agenda :snake:  Em construção...  🚧 </h5>

<p align="center"><a href="#instalacao">Instalação</a> • <a href="#rodando">Rodando o Server</a> • <a href="#tecnologias">Tecnologias</a> • <a href="#template">Template</a> • <a href="#demonstracao">Demonstração</a></p>

<h2 id="instalacao">Instalação:</h2>
<h5>Pré-requisito:</h5>

Antes de começar, você vai precisar ter em sua máquina o [Git](https://git-scm.com) instalado.<br>
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

<h5 id="rodando">🎲 Rodando o Back End (servidor):</h5>

```
# Clone este repositório
git clone < https://github.com/Anderson-S-M3/agenda_django.git >

# Acesse a pasta do projeto no terminal/cmd
cd agenda_django

# crie uma Venv
python -m venv <nome_da_venv>

#Ative a Venv
cmd: "<nome_da_venv>/Scripts/activate"
terminal: source <nome_da_venv>/bin/activate

# Instale o Django e o Pillow
pip install Django==2.2.16
pip install Pillow

# Instale as dependências
manage.py makemigrations
manage.py migrate

# Execute a aplicação
manage.py runserver

# O servidor inciará na porta:8000 - acesse < http://localhost:8000 >
```

<h2 id="tecnologias">🛠 Tecnologias</h2>
<p>As seguintes ferramentas foram usadas na construção do projeto:</p>

- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font_Awesome](https://fontawesome.com/)

<h2 id="template">Template</h2>
<p>Link do template utilizado no projeto:</p>

- [Login](https://bootsnipp.com/snippets/dldxB)

<h2 id="demonstracao">Demonstração</h2>

<p>Demonstração e codigo:</p>

<p><b>Barra de Busca:</b></p>
<img src="https://user-images.githubusercontent.com/65872811/101603448-59613d80-39de-11eb-83e6-b061a2dd11c0.gif" alt="exemplo seatch_field">

```
usuario = request.user
try:
    #Pesquisar
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.filter(usuario=usuario).annotate(
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
```

<br>

<p><b>Pagination:</b></p>
<img src="https://user-images.githubusercontent.com/65872811/101688394-ba265f80-3a4a-11eb-98d7-3670ea9208b6.gif" alt="exemplo seatch_field">

```
paginator = Paginator(contatos, 1)  # Mostra 1 contato por pagina
page = request.GET.get('page')
contatos = paginator.get_page(page)
```

<br>
<br>

## 📝 Licença
---

Este projeto esta sobe a licença [MIT](./LICENSE.md).

<br>
<br>

### Autor
---

Feito com ❤️ por Anderson S. 👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/Anderson_S-0077B5?style=for-the-badge&logo=linkedin&logoColor=white/)](https://www.linkedin.com/in/anderson-s-antunes-b879251b9/) <br>
[![Email](https://img.shields.io/badge/Anderson__S__Antunes@hotmail.com-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:anderson_s_antunes@hotmail.com)
