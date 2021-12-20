from django.urls import path
from .views import FruitList, FruitsModify, Authenticate, signup

urlpatterns = [
    path('api/<str:keys>', FruitList.as_view()),
    path('', Authenticate),
    path('get', FruitsModify.as_view()),
    path('signup', signup, name='signup')
]