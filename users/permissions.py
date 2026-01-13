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
