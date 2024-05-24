from django.urls import path, include
from rest_framework import routers
from api_prueba2 import views


router = routers.DefaultRouter()
router.register(r'api_backen', views.restauranteView, 'api_backen' )

urlpatterns = [
    path("", include (router.urls) ),
   
    
]
