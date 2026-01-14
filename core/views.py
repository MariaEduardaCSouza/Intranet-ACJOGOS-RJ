from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.permissions import require_diretoria

@login_required
def home(request):
    """
    Página inicial acessível apenas para usuários autenticados.
    
    """
    user = request.user
    context = {
        'tipo_usuario': user.tipo_usuario,
    }
    
    return render(request, 'home.html')

def area_diretoria(request):
    require_diretoria(request.user)
    return render(request, 'diretoria.html')