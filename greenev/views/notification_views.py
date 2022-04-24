
from rest_framework.decorators import api_view
from rest_framework.response import Response

from greenev.models import Evenementnotif,Alertnotif
from greenev.serializers import EvenementnotifSerializer,AlertnotifSerializer



@api_view(['GET'])
def alertNotifList(request):
    alertnotif=Alertnotif.objects.all()
    serializer=AlertnotifSerializer(alertnotif,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def evenementNotifList(request):
    evenementnotif=Evenementnotif.objects.all()
    serializer=EvenementnotifSerializer(evenementnotif,many=True)
    return Response(serializer.data)
