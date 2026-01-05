from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    """
    Página inicial acessível apenas para usuários autenticados.
    
    """
    return render(request, 'home.html')