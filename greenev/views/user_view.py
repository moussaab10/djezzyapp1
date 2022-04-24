from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from rest_framework import status

from greenev.models import User

from greenev.serializers import UserSerializer2, UserSerializerWithToken,allUserSerializer,UserSerializer3
from django.db.models import Q


# connection view


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addAdmin(request):
    # serializer =UserSerializer2(data = request.data)
    # serializer.save()
    # return Response(serializer.data)

    data = request.data
    print(data)
    try:
        user = User.objects.create(
            username=data['username'],
            is_staff=data['is_staff'],
            GradeState=data['GradeState'],
            password=make_password(data['password'])
        )

        serializer = UserSerializer3(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this username already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allUsers(request):
    user = User.objects.exclude(GradeState='AUCUN')
    serializer = allUserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):

    user = request.user
    serializer = UserSerializer2(user, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delteUsers(request, pk):

    user = User.objects.get(id=pk)
    user.delete()
    return Response('user deleted')


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, pk):

    user = User.objects.get(id=pk)
    serializer = allUserSerializer(user, many=False)
    return Response(serializer.data)



@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateUser(request):
    data = request.data
    user = User.objects.get(id=data['id'])

    user.username = data['username']
    user.GradeState = data['GradeState']
    user.is_staff = data['is_staff']

    user.save()
    serializer = allUserSerializer(user, many=False)

    return Response("L'utilisateur a été mis à jour")
