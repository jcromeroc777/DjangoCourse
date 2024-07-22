from datetime import timezone

from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(max_length=300, label="Descripción")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, label="Disponible", required=False)
    image = forms.ImageField(label="Imagen", required=False)

    def save(self):
        data = self.cleaned_data
        product = Product(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            available=data.get("available"),
            image=data.get("image"),
        )
        product.save()
        return product

    def __str__(self):
        return self.name