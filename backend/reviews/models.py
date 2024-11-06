from django.db import models
from django.conf import settings

class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='resenas')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resenas')
    contenido = models.TextField()
    calificacion = models.PositiveIntegerField()  # Asume calificación de 1 a 5
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reviews' 
