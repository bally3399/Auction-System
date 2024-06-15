from django.urls import path
from . import views

urlpatterns = [
    path('auctions', views.list_items)
]
