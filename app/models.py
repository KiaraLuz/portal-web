from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Empleado(models.Model):
    ROLES = (
        ('Gerente', 'Gerente'),
        ('Desarrollador', 'Desarrollador'),
        ('Recursos Humanos', 'Recursos Humanos'),
        ('Ventas', 'Ventas'),
    )
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=50, choices=ROLES)
    departamento = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    telefono = models.CharField(max_length=15)
    
    # Agregando una clave foránea al modelo User
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.rol})'
