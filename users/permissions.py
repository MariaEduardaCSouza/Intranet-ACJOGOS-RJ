"""
Permissões personalizadas para o modelo de usuário.
Regras de acesso baseadas no tipo de usuário.
"""

def is_diretoria(user):
    """
    Verifica se o usuário é do tipo 'DIRETORIA'.
    """
    return user.is_authenticated and user.tipo_usuario == 'DIRETORIA'

def is_associado(user):
    """
    Verifica se o usuário é do tipo 'ASSOCIADO'.
    """
    return user.is_authenticated and user.tipo_usuario == 'ASSOCIADO'

def is_afiliado(user):
    """
    Verifica se o usuário é do tipo 'AFILIADO'.
    """
    return user.is_authenticated and user.tipo_usuario == 'AFILIADO'

def is_coletivo(user):
    """
    Verifica se o usuário é do tipo 'COLETIVO'.
    """
    return user.is_authenticated and user.tipo_usuario == 'COLETIVO'

def require_diretoria(user):
    """
Garante acesso apenas para usuários do tipo 'DIRETORIA'

    """
    if not is_diretoria(user):
        raise PermissionError("Acesso negado: apenas para Diretoria.")
    
def require_associado(user):
    """
    Garante acesso apenas para usuários do tipo 'ASSOCIADO'.
    """
    if not is_associado(user):
        raise PermissionError("Acesso negado: apenas para Associados.")

def require_authenticated(user):
    """
    Garante que o usuário esteja autenticado.
    """
    if not user.is_authenticated:
        raise PermissionDenied("Usuário não autenticado.")