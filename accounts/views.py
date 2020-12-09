from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    if not request.method == 'POST':
        return render(request, 'accounts/login.html')

    username = request.POST['usuario']
    password = request.POST['senha']
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        messages.info(request,'Logado com sucesso')
        return redirect('index_contatos')
    else:
        messages.error(request,'Usuario ou Senha não encontrados')
        return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('index_contatos')


def register_view(request):
    if not request.method == 'POST':
        return render(request, 'accounts/register.html')

    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    email = request.POST['email']

    username = request.POST['usuario']
    senha = request.POST['senha']
    senha2 = request.POST['senha2']
    
    if len(nome) <=1:  # Validar NOME
        messages.info(request, 'Nome Obrigatorio')
        return redirect('register')
    
    try:  # Validar E-MAIL
        validate_email(email)
    except:
        messages.error(request,'E-mail invalido')
        return redirect('register')
    
    if len(username) <=6:  # Validar USUARIO
        messages.info(request, 'Usuario deve conter 7 caracteres ou mais')
        return redirect('register')
    
    if len(senha) <=6:  # Validar Senhas
        messages.info(request, 'Senha deve conter 7 caracteres ou mais')
        return redirect('register')
    
    elif senha != senha2:  # Verificar igualdade
        messages.warning(request, 'As Senhas Devem ser iguais')
        return redirect('register')     

    if User.objects.filter(username=username).exists():  # Verificar usuario
        messages.error(request, 'Usuario já cadastrado')
        return redirect('register') 
    
    elif User.objects.filter(email=email).exists():  # Verificar e-mail
        messages.error(request, 'E-mail ja cadastrado')
        return redirect('register')      

    else:
        user = User.objects.create_user(
        first_name=nome,
        last_name=sobrenome,
        email=email,
        username=username,
        password=senha
        )
        user.save()
        return redirect('login')
