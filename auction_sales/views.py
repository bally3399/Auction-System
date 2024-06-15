from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item
from .serializers import ItemSerializer


# Create your views here.

@api_view()
def list_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
