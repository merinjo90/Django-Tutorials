
from django.shortcuts import render
from .models import *
from .serializers import *


# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({'sucess': 'hurray you are authenticate'})



class ProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
