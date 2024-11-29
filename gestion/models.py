from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=(100),unique=True,help_text="Elija una opciòn")
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=(100))
    precio = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=0)

    
    def __str__(self):
        return self.nombre
    