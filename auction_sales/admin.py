from django.contrib import admin

from .models import Item


# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_number', 'item_name', 'item_description', 'item_amount', 'item_status']