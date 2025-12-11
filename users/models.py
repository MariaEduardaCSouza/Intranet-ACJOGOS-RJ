from django.db import models
from django.contrib.auth.models import (AbstractUser, PermissionsMixin, BaseUserManager
)

class UserType(models.TextChoices):
    DIRETORIA = 'DIRETORIA', 'Diretoria'
    ASSOCIADO = 'ASSOCIADO', 'Associado'
    AFILIADO = 'AFILIADO', 'Afiliado'
    COLETIVO = 'COLETIVO', 'Coletivo'
    
class UserManager(BaseUserManager):
    """
    Gerencia a criação de usuários e superusuários.
    O login é baseado no e-mail.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Cria e salva um usuário com o e-mail e senha fornecidos.
        """
        if not email:
            raise ValueError('O e-mail deve ser fornecido')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Cria e salva um superusuário com o e-mail e senha fornecidos.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuários devem ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuários devem ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

