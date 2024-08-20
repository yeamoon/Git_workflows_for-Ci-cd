from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Productowner
from .serializers import ProductownerSerializer

class ProductownerListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Productowner.objects.all()
    serializer_class = ProductownerSerializer
   

class ProductownerView(RetrieveAPIView):
    queryset = Productowner.objects.all()
    serializer_class = ProductownerSerializer

class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset =Productowner.objects.filter(top_seller=True)
    serializer_class = ProductownerSerializer
   