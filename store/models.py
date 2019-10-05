from django.db import models
from random import randint

# Create your models here.


class Product(models.Model):
    upccode = models.CharField('UPC code', max_length=14)
    description = models.CharField('Description', max_length=60)
    quantitiy = models.IntegerField('Quantity')
    price = models.DecimalField("Unit Price",
                                max_digits=9, decimal_places=2)

    def __str__(self):
        return self.upccode

    def quantity_in_stock(self):
        """Compute and return number of units in stock"""
        return randint(0, 100)
