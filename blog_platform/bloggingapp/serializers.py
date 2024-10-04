from rest_framework import serializers  
from .models import Product  
  
class ProductSerializer(serializers.ModelSerializer):  
  class Meta:  
      model = Product  
      fields = ['name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_date']



from rest_framework import serializers  
from .models import User  
  
class UserSerializer(serializers.ModelSerializer):  
  class Meta:  
    model = User  
    fields = ['username', 'email', 'password']
