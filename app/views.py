from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.serializers import ItemSerializer
from app.models import TodoItem
from django.utils import timezone

# Create your views here.

# For view all items
@api_view(['GET'])
def all_details(request):
    items = TodoItem.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

# For Create Item
@api_view(['POST'])
def create_detail(request):
    item = ItemSerializer(data=request.data)
    if item.is_valid():
        item.save()
    return Response(item.data)

# For update Item
@api_view(['POST'])
def update_detail(request, pk):
    item = TodoItem.objects.get(id=pk)
    serializer  = ItemSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save(updated = timezone.now())
    return Response(serializer.data)

# For delete Item
@api_view(['DELETE'])
def delete_detail(request, pk):
    print(pk)
    item = TodoItem.objects.get(id=pk)
    item.delete()
    return Response("deleted")