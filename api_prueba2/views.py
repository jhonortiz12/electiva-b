from .models import restaurante 
from rest_framework import viewsets
from .serializer import restauranteSerializer


class restauranteView(viewsets.ModelViewSet):
    serializer_class = restauranteSerializer
    queryset = restaurante.objects.all()
    
    

# Create your views here.
