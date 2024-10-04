from django.shortcuts import render
from rest_framework import viewsets  
from .models import Product  
from .serializers import ProductSerializer  
  
class ProductViewSet(viewsets.ModelViewSet):  
   queryset = Product.objects.all()  
   serializer_class = ProductSerializer
   
from rest_framework import viewsets  
from .models import User  
from .serializers import UserSerializer  
  
class UserViewSet(viewsets.ModelViewSet):  
  queryset = User.objects.all()  
  serializer_class = UserSerializer

# Create your views here.
