import enum

from django.db import models

# Create your models here.


class Role(models.TextChoices):
    SELLER = "S", "SELLER"
    BIDDER = "D", "BIDDER"


class Status(models.TextChoices):
    UPCOMING = "U", "UPCOMING"
    ONGOING = "O", "ONGOING"
    CLOSED = "C", "CLOSED"


class User(models.Model):
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=100,blank=False)
    user_name = models.CharField(max_length=255,blank=False)
    is_logged_in = models.BooleanField
    pass_word = models.CharField(max_length=255,blank=False)
    email = models.EmailField(max_length=255,blank=False)
    ROLE = models.CharField(max_length=50,choices=Role.choices)
    id=models.FloatField
    date_added = models.DateTimeField(auto_now=True)


class Category(models.Model):
    ANTIQUES = "A", "ANTIQUES",
    ART = "ART", "ART",
    BOOK = "B", "BOOK",
    JEWELRY = "JEWELRY", 'JEWELRY'
    SPORT = 'SPORT', 'SPORT'
    FASHION = 'WINE', 'WINE'
    WINE = 'WINE', 'WINE'


class Bid(models.Model):
    id = models.AutoField
    item_name = models.CharField(max_length=255,blank=False)
    item_category = models.CharField(max_length=50,blank=False)
    bidder = models.CharField(max_length=50,blank=False)
    starting_price = models.DecimalField(default=0.00)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()




class Items(models.Model):
    id = models.AutoField
    item_name = models.CharField(max_length=255, blank=False)
    item_Category = models.CharField(max_length=50,choices=Role.choices)
    item_status = models.CharField(max_length=50,choices=Role.choices)
    item_amount = models.DecimalField(default=0.00)
    bids = models.ManyToManyField(Bid)





