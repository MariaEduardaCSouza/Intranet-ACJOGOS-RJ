from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''
    Configuração do admin para o modelo User.
    Exibe e permite a edição dos campos principais do usuário.
    '''
    list_display = ('email','nome', 'tipo_usuario', 'is_active', 'is_staff')
    search_fields = ('email', 'nome', 'cpf')
    list_filter = ('tipo_usuario', 'is_active', 'is_staff')