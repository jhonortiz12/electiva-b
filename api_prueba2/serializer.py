from rest_framework import serializers
from .models import restaurante

class restauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurante
        fields ='__all__'