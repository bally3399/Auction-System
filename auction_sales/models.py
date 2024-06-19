from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(max_length=55, primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    ROLE = [
        ('S', 'SELLER'),
        ('B', 'BIDDER')
    ]
    role = models.CharField(max_length=1, choices=ROLE, default='B')
    is_logged_in = models.BooleanField(default=False)


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    ITEM_CATEGORY = [
        ('F', 'FURNITURE'),
        ('E', 'ELECTRONICS'),
        ('FASH', 'FASHION'),
        ('A', 'ANTIQUES'),
        ('AR', 'ART'),
        ('B', 'BOOK'),
        ('JEW', 'JEWELRY'),
        ('S', 'SPORT'),
        ('W', 'WINE')
    ]
    ITEM_STATUS = [
        ('UP', 'UPCOMING'),
        ('ON', 'ONGOING'),
        ('CL', 'CLOSED')
    ]
    item_amount = models.DecimalField(max_digits=10, decimal_places=2)
    item_category = models.CharField(max_length=4, choices=ITEM_CATEGORY, default='F')
    item_status = models.IntegerField(max_length=2, choices=ITEM_STATUS, default='NS')


class Admin(models.Model):
    id = models.IntegerField(max_length=55, primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_logged_in = models.BooleanField(default=False)


class Bid(models.Model):
    id = models.AutoField(primary_key =True, unique=True)
    item_name = models.CharField(max_length=100)
    bidder = models.CharField(max_length=100)
    ITEM_CATEGORY = [
        ('F', 'FURNITURE'),
        ('E', 'ELECTRONICS'),
        ('FASH', 'FASHION'),
        ('A', 'ANTIQUES'),
        ('AR', 'ART'),
        ('B', 'BOOK'),
        ('JEW', 'JEWELRY'),
        ('S', 'SPORT'),
        ('W', 'WINE')
    ]
    item_category = models.CharField(max_length=4, choices=ITEM_CATEGORY, default='F')
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
