from django.db import models
from django.contrib.auth.models import (AbstractUser, PermissionsMixin, BaseUserManager
)

class UserType(models.TextChoices):
    DIRETORIA = 'DIRETORIA', 'Diretoria'
    ASSOCIADO = 'ASSOCIADO', 'Associado'
    AFILIADO = 'AFILIADO', 'Afiliado'
    COLETIVO = 'COLETIVO', 'Coletivo'
    PUBLICO = 'PUBLICO', 'Público'
    
    
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

class User(AbstractUser, PermissionsMixin):
    """
    Modelo de usuario da plataforma ACJOGOS-Rj.
    Recebe os dados da pessoa física: nome, e-mail, CPF, telefone, endereço, etc.
    """
    #dados de logiin
    email = models.EmailField(
        unique=True,
        help_text='E-mail do usuário.'
        )
    
    #dados pessoais
    nome = models.CharField(
        max_length=150,
        help_text='Nome completo do usuário.'
        )
    
    cpf = models.CharField(
        max_length=14,
        unique=True,
        help_text='CPF do usuário.'
        )
    
    telefone = models.CharField(
        max_length=15,
        blank=True,
        help_text='Telefone de contato do usuário.'
        )
    
    nick_discord = models.CharField(
        max_length=50,
        blank=True,
        help_text='Nick do Discord do usuário.' 
        )
    cep = models.CharField(max_length=9,help_text='CEP do endereço do usuário.')
    numero = models.CharField(max_length=10,help_text='Número do endereço do usuário.')
    complemento = models.CharField(max_length=50, blank=True, help_text='Complemento do endereço do usuário.')
    bairro = models.CharField(max_length=50, help_text='Bairro do endereço do usuário.')
    cidade = models.CharField(max_length=50, help_text='Cidade do endereço do usuário.')
    estado = models.CharField(max_length=2, help_text='Estado do endereço do usuário    .') 
    
    tipo_usuario = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.PUBLICO,
        help_text='Tipo do usuário na plataforma.'
        )
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)   
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cpf']
    
    def __str__(self):
        return self.email