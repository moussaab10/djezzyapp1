
from rest_framework.decorators import api_view
from rest_framework.response import Response

from greenev.models import Review
from greenev.serializers import ReviewSerializer


    
@api_view(['GET'])
def reviewList(request):
    review=Review.objects.all()
    serializer=ReviewSerializer(review,many=True)
    return Response(serializer.data) 

