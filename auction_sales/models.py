from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=50, unique=True, null=False, blank=False)
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    ROLE = [
        ('S', 'SELLER'),
        ('B', 'BIDDER')
    ]
    role = models.CharField(max_length=1, choices=ROLE, blank=False, null=False)
    is_logged_in = models.BooleanField(default=False)


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
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
    item_category = models.CharField(max_length=4, choices=ITEM_CATEGORY, default='A', null=False, blank=False)
    item_status = models.CharField(max_length=2, choices=ITEM_STATUS, default='UP', null=False, blank=False)


class Admin(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, unique=True, null=False, blank=False)
    username = models.CharField(max_length=100, blank=False, null=False, unique=True)
    password = models.CharField(max_length=20, null=False, blank=False)
    is_logged_in = models.BooleanField(default=False)


class Bid(models.Model):
    id = models.AutoField(primary_key=True)
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
    bidder_name = models.CharField(max_length=180, blank=False, null=False)

