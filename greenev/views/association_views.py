
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from greenev.models import Association
from greenev.serializers import AssociationSerializer
from greenev.models import User


    
@api_view(['GET'])
def associationList(request):
    association=Association.objects.all()
    serializer=AssociationSerializer(association,many=True)
    return Response(serializer.data) 


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delteAssociation(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('user deleted')


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getAssociationById(request, pk):

    user = User.objects.get(id=pk)
    association = Association.objects.get(user=user)
    serializer = AssociationSerializer(association, many=False)
    return Response(serializer.data)

# update association


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateStateAssociation(request):
    data = request.data
    user = User.objects.get(id=data['id'])
    association = Association.objects.get(user=user)

    association.associationState = data['associationState']
    association.dossiertState = data['dossiertState']

    association.save()
    serializer = AssociationSerializer(association, many=False)

    return Response("L'Association a été mis à jour")
