from django.db import models


# Create your models here.
class FoodSale(models.Model):
    date = models.DateField()
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


