from django.urls import path, include
from rest_framework import routers
from api_prueba2 import views


router = routers.DefaultRouter()
router.register(r'restaurante', views.restauranteView, 'restaurante' )

urlpatterns = [
    path("api/", include (router.urls) ),
   
    
]
