from django.db import models
from .utility import generate_item_number


# Create your models here.

class Item(models.Model):
    item_number = models.CharField(max_length=3, default=generate_item_number, unique=True, primary_key=True)
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    ITEM_STATUS = [
        ('SO', 'SOLD'),
        ('NS', 'NOT SOLD'),
    ]
    item_status = models.CharField(max_length=2, choices=ITEM_STATUS, default='NS')
    item_amount = models.DecimalField(max_digits=9, decimal_places=2)
