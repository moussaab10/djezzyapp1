
from rest_framework.decorators import api_view
from rest_framework.response import Response

from greenev.models import Alert
from greenev.serializers import AlertSerializer



@api_view(['GET'])
def alertList(request):
    alert=Alert.objects.all()
    serializer=AlertSerializer(alert,many=True)
    return Response(serializer.data)
