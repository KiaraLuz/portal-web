from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    ROLES = (
        ('Gerente', 'Gerente'),
        ('Desarrollador', 'Desarrollador'),
        ('Recursos Humanos', 'Recursos Humanos'),
        ('Vendedor', 'Vendedor'),
    )
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=50, choices=ROLES)
    departamento = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    telefono = models.CharField(max_length=15)
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.rol})'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    cantidad_vendida = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.nombre} ({self.categoria})'