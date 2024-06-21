from django.urls import path
from . import views

urlpatterns = [
    path('auction', views.list_item),
]
