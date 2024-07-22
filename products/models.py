from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(max_length=300, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    image = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name="Imagen"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    def __str__(self):
        return self.name
