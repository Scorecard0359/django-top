from django.db import models

class Category:
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product:
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=5, unique=True)
    category = models.ForeignKey('shop.models.Category', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.code} - {self.name}"