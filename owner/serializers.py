from rest_framework import serializers
from .models import Productowner

class ProductownerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productowner
        fields = '__all__'