
from rest_framework.decorators import api_view,permission_classes

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from greenev.models import Evenement
from greenev.serializers import EvenementSerializer


    
@api_view(['GET'])
def evenementList(request):
    evenement=Evenement.objects.all()
    serializer=EvenementSerializer(evenement,many=True)
    return Response(serializer.data) 


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getEvenementById(request, pk):

    evenement = Evenement.objects.get(id=pk)

    serializer = EvenementSerializer(evenement, many=False)
    return Response(serializer.data)

