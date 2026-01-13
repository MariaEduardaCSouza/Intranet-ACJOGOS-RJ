from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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