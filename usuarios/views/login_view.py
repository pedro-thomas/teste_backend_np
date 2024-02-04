from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('base_page')  # Redireciona para a página de login para teste
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos')
    
    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')