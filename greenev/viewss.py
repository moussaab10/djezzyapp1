from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Citoyen
from .serializers import CitoyenSerializer



@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/users/',
    }
    return Response(api_urls)


@api_view(['GET'])
def citoyenList(request):
    citoyen=Citoyen.objects.all()
    serializer=CitoyenSerializer(citoyen,many=True)
    return Response(serializer.data) 