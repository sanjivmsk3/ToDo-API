from django.db.models import fields
from rest_framework import serializers
from app.models import TodoItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('__all__')