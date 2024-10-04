from rest_framework import serializers  
from .models import Product  
  
class ProductSerializer(serializers.ModelSerializer):  
  class Meta:  
   model = Product  
   fields = ['name', 'description', 'category', 'stock_quantity', 'image_url', 'created_date']

