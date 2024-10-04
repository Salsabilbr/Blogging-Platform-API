from django.db import models  
  
class Product(models.Model):  
  name = models.CharField(max_length=255)  
  description = models.TextField()  
  price = models.DecimalField(max_digits=10, decimal_places=2)  
  category = models.CharField(max_length=255)  
  stock_quantity = models.IntegerField()  
  image_url = models.URLField()  
  created_date = models.DateTimeField(auto_now_add=True)  
  
  def __str__(self):  
   return self.name

from django.db import models  
  
class User(models.Model):  
  username = models.CharField(max_length=255)  
  email = models.EmailField(unique=True)  
  password = models.CharField(max_length=255)  
  
def __str__(self):  
   return self.username


# Create your models here.
