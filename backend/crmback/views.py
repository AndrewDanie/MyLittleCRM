from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class OrderAPIList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerialiser