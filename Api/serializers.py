from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Fruits

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        #This is a serializer includes all the available models by using the __all__ rsther than specifying the models
        fields = 'id', 'name', 'benefit', 'date_updated'