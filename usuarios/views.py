from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
import re

def cadastro(request):
    return render(request, 'cadastro.html')

def perfil(request):
    return render(request, 'perfil.html')

def perfil_with_user(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
        return render(request, 'perfil.html', {'usuario': usuario})
    except Usuario.DoesNotExist:
        return render(request, 'perfil.html', {'usuario': None})

def valida_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Verifica se o email já está em uso
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este email já está em uso. Por favor, utilize outro.')
            return redirect('login')  # Redireciona para a página de login
            
        # Verifica se algum campo está vazio
        if not nome.strip() or not email.strip() or not senha:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return redirect('login')  # Redireciona para a página de login
            
        # Verifica se a senha atende aos critérios mínimos
        if len(senha) < 8 or not re.search("[A-Z]", senha) or not re.search("[a-z]", senha) or not re.search("[0-9]", senha) or not re.search("[!@#$%^&*]", senha):
            messages.error(request, 'A senha não atende aos critérios mínimos.')
            return redirect('login')  # Redireciona para a página de login
            
        try:
            # Cria o usuário no banco de dados
            usuario = Usuario.objects.create(nome=nome, email=email, senha=senha)
            messages.success(request, 'Cadastro realizado com sucesso!')
            
            # Redireciona para a página de perfil com os detalhes do usuário
            return redirect('perfil_with_user', pk=usuario.pk)
        except Exception as e:
            print(e)
            messages.error(request, 'Houve um erro no cadastro. Tente novamente.')
    
    return redirect('login')  # Redireciona para a página de login em caso de método incorreto
