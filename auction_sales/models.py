from django.db import models


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=180, blank=False, null=False)
    last_name = models.CharField(max_length=180, blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    password = models.CharField(max_length=15, null=False, blank=False)
    is_logged_in = models.BooleanField(default=False)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=180, blank=False, null=False)
    last_name = models.CharField(max_length=180, blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    ROLE = [
        ('SELLER', 'Seller'),
        ('BIDDER', 'Bidder')
    ]
    role = models.CharField(max_length=6, choices=ROLE, blank=False, null=False)
    password = models.CharField(max_length=15, null=False, blank=False)
    is_logged_in = models.BooleanField(default=False)


# class Seller(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=180, blank=False, null=False)
#     last_name = models.CharField(max_length=180, blank=False, null=False)
#     email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
#     username = models.CharField(max_length=30, unique=True, null=False, blank=False)
#     password = models.CharField(max_length=15, null=False, blank=False)
#     is_logged_in = models.BooleanField(default=False)
# last_seen_date = models.DateField(default=datetime.date.today)

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=180, blank=False, null=False)
    item_price = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    ITEM_STATUS = [
        ('UPCOMING', 'Upcoming'),
        ('ONGOING', 'Ongoing'),
        ('ENDED', 'Ended')
    ]
    item_status = models.CharField(max_length=8, choices=ITEM_STATUS, blank=False, null=False)
    ITEM_CATEGORY = [
        ('ANTIQUES', 'Antiques'),
        ('ART', 'Art'),
        ('BOOKS', 'Books'),
        ('FASHION', 'Fashion'),
        ('JEWELLERY', 'Jewellery'),
        ('SPORTS', 'Sports'),
        ('WINE', 'Wine'),
        ('OTHERS', 'Others')
    ]
    item_category = models.CharField(max_length=9, choices=ITEM_CATEGORY, blank=False, null=False)


class Bid(models.Model):
    bid_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=180, blank=False, null=False)
    item_category = models.CharField(max_length=180, blank=False, null=False)
    starting_price = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    bidder_name = models.CharField(max_length=180, blank=False, null=False)

# class Bid(models.Model):
#     id = models.AutoField(primary_key=True)
#     bidder = models.ForeignKey(Bidder)
#     item = models.ForeignKey(Item)
