from django.urls import path
from .views import FruitList, FruitsModify

urlpatterns = [
    path('', FruitList.as_view()),
    path('get', FruitsModify.as_view())
]