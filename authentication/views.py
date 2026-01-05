from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    '''
    view responsável por autenticar usuários na plataforma via e-mail e senha.
    '''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user:
            login(request, user)
            return redirect('home')  #Ajustar depois para a página inicial correta
        return render(
            request, 'login.html',
            {'error': 'E-mail ou senha inválidos.'}
        )
                   
def logout_view(request):
    '''
    view responsável por deslogar usuários da plataforma.
    '''
    logout(request)
    return redirect('login')