from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Fruits
from .serializers import FruitSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
# Create your views here.

#The following views are written with class based views

class FruitList(APIView):
    def get(self, request):
        fruit = Fruits.objects.all()
        fruit_accord = fruit.order_by('name')
        fruit_content = FruitSerializer(fruit_accord, many=True)
        return JsonResponse(fruit_content.data, safe=False)
        #return Response(fruit_content.data, status=status.HTTP_200_OK)
    def post(self, request):
        fruit = Fruits.objects.all()
        new_fruit_object = FruitSerializer(fruit, data=request.data)
        if new_fruit_object.is_valid():
            new_fruit_object.save()
            return Response(new_fruit_object.data)
        return Response(new_fruit_object.errors, status=status.HTTP_400_BAD_REQUEST)
class FruitsModify(APIView):
    def get_object(self, title):
        fruit = Fruits.objects.get(title=title)
        return fruit
    def get(self, request, title):
        fruits = self.get_object(title)
        return Response(fruits.data, status=status.HTTP_200_OK)
    def put(self, request, title):
        fruit = self.get_object(title)
        fruits = FruitSerializer(fruit, data=request.data)
        if fruits.is_valid():
            fruits.save()
            return Response(fruits.data, status=status.HTTP_202_ACCEPTED)
    def delete(self, request, title):
        fruit = self.get_object(title)
        fruit.delete()
        return Response(status=status.HTTP_200_OK)