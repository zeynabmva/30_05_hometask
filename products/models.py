from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)