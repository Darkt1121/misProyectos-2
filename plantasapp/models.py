from django.db import models

# Create your models here.

# Para las flores
class Flor(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    fecha_disponibilidad = models.DateField()
    # que devuelva el nombre
    def __str__(self):
        return self.nombre
# Para tierra de hoja

class Tierra(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    fecha_disponibilidad = models.DateField()
    # que devuelva el nombre
    def __str__(self):
        return self.nombre
    
# Para macetero

class Macetero(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    fecha_disponibilidad = models.DateField()
     # que devuelva el nombre
    def __str__(self):
        return self.nombre
    