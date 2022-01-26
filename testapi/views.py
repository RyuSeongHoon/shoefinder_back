from logging import exception
import random
import string
import pdb
from django.http import request

from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView, View
from rest_framework.response import Response 
from django.http.response import HttpResponse 

from .models import Test
from .serializers import TestSerializer
from django.core import serializers
from django.http import JsonResponse

class TestViewSet(viewsets.ModelViewSet):
        
    queryset = Test.objects.all()
    # queryset = Test.objects.filter(sub_id=id)
    
    serializer_class = TestSerializer


def article_list(request, slug):
    queryset = Test.objects.filter(sub_id=slug)# .values()
    queryset_json = serializers.serialize('json',queryset)

    # serializer = TestSerializer(queryset, many=True)
    return HttpResponse(queryset_json)