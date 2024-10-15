from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class CustomUser(AbstractUser):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
  
    bio = models.TextField(max_length=500, blank=True, null=True, help_text="Biografía o descripción del usuario.")
    birth_date = models.DateField(null=True, blank=True, help_text="Fecha de nacimiento del usuario.")
    
    address = models.CharField(max_length=255, blank=True, null=True, help_text="Dirección de residencia.")
    city = models.CharField(max_length=100, blank=True, null=True, help_text="Ciudad de residencia.")
    postal_code = models.CharField(max_length=20, blank=True, null=True, help_text="Código postal.")
    country = models.CharField(max_length=100, blank=True, null=True, help_text="País de residencia.")
    
    
    USER_ROLES = (
        ('cliente', 'Cliente'),
        ('vendedor', 'Vendedor'),
        ('admin', 'Administrador'),
    )
    role = models.CharField(max_length=20, choices=USER_ROLES, default='cliente', help_text="Rol del usuario en la plataforma.")
    
    
    registration_date = models.DateTimeField(auto_now_add=True, help_text="Fecha de registro del usuario.")
    last_update = models.DateTimeField(auto_now=True, help_text="Última actualización de los datos del usuario.")
    
    def __str__(self):
        return self.username
