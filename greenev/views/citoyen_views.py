
from rest_framework.decorators import api_view,permission_classes

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from greenev.models import Citoyen,User
from greenev.serializers import *

# get all citoyen

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allCitoyens(request):
    citoyen=Citoyen.objects.all()
    serializer=CitoyenSerializer(citoyen,many=True)
    return Response(serializer.data)



# delete citoyen
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delteCitoyen(request, pk):

    user = User.objects.get(id=pk)
    user.delete()
    return Response('user deleted')

# get one citoyen

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getCitoyenById(request, pk):

    user = User.objects.get(id=pk)
    citoyen = Citoyen.objects.get(user=user)

    serializer = CitoyenSerializer(citoyen, many=False)
    return Response(serializer.data)

# update citoyens


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateStateCitoyen(request):
    data = request.data
    user = User.objects.get(id=data['id'])
    citoyen = Citoyen.objects.get(user=user)

    citoyen.CitezenState = data['CitezenState']

    citoyen.save()
    serializer = CitoyenSerializer(citoyen, many=False)

    return Response("L'utilisateur a été mis à jour")
