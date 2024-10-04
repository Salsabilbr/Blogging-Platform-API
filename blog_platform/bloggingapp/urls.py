
from django.urls import path  
from rest_framework import routers  
from . import views  
  
router = routers.DefaultRouter()  
router.register(r'products', views.ProductViewSet)  
  
urlpatterns = [  
  path('', include(router.urls)),  
]


from django.urls import path  
from rest_framework import routers  
from . import views  
  
router = routers.DefaultRouter()  
router.register(r'users', views.UserViewSet)  
  
urlpatterns = [  
  path('', include(router.urls)),  
]

