from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Fruits
from .serializers import FruitSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
#from django.contrib.auth import authenticate
# Create your views here.

# The following views are written with class based views


def signup(request):
    return render(request, 'contact.html')


def Authenticate(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        username = request['username']
        password = request['password']
        user = User.objects.get(username=username, password=password)
        if user.is_authenticated:
            return render(request, 'home.html')
        return render(request, 'index.html', context={'message': 'Password and Username does not match'})


class FruitList(APIView):
    authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]

    def get_token(self, request, keys):
        token = keys
        return token

    def get(self, request, keys):
        token_gotten = self.get_token(request, keys)
        token_str = str(token_gotten)
        print(token_gotten)
        try:
            Chk_Token = Token.objects.get(key=token_gotten)
            print(Chk_Token)
        except ObjectDoesNotExist:
            return JsonResponse('{error: Invalid Credentials}', safe=False)
        fruit = Fruits.objects.all()
        fruit_accord = fruit.order_by('name')
        fruit_content = FruitSerializer(fruit_accord, many=True)
        return JsonResponse(fruit_content.data, safe=False)
        #return JsonResponse('Invalid Credentials')
        # return Response(fruit_content.data, status=status.HTTP_200_OK)

    def post(self, request):
        fruit = Fruits.objects.all()
        new_fruit_object = FruitSerializer(fruit, data=request.data)
        if new_fruit_object.is_valid():
            new_fruit_object.save()
            return Response(new_fruit_object.data)
        return Response(new_fruit_object.errors, status=status.HTTP_400_BAD_REQUEST)


class FruitsModify(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
