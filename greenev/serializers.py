from .models import Evenement, Association, Citoyen, Alert, Review, Alertnotif, Evenementnotif, User,dossier
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

# all


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# customiz

class allUserSerializer(serializers.ModelSerializer):
    last_login = serializers.SerializerMethodField(read_only=True)
    date_creat = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'online', 'last_login','date_creat', 'is_staff', 'GradeState','image']

    def get_last_login(self, obj):
        date = str(obj.last_login)
        return date[0:10]

    def get_date_creat(self, obj):
        date = str(obj.date_joined)
        return date[0:10]


class UserSerializer2(serializers.ModelSerializer):
    last_login = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'online', 'last_login', 'is_staff', 'GradeState']

    def get_last_login(self, obj):
        date = str(obj.last_login)
        return date[0:10]


class UserSerializerWithToken(UserSerializer2):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'online','last_login', 'is_staff', 'GradeState', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)



class UserSerializer3(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff', 'GradeState','password']



# --------------------------------------------------------
# class CitoyenUserAlert(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ['id', 'username','email','first_name','last_name','image','online']

class CitoyenUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username','email','first_name','last_name','image','online']

class CitoyenSerializer(serializers.ModelSerializer):
    user = CitoyenUser(required=True)
    class Meta:
        model = Citoyen
        fields = '__all__'


class UsernameId(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
class Citoyen1(serializers.ModelSerializer):
    user = UsernameId(required=True)
    class Meta:
        model = Citoyen
        fields = ['user']
class Association1(serializers.ModelSerializer):
    user = UsernameId(required=True)
    class Meta:
        model = Association
        fields = ['user']

class Alert1(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['latitude','longitude','wilaya','commune','ville']

# -----------------------------------------------------------
class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = dossier
        fields = '__all__'
class AssociationUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email','image','online']
class AssociationSerializer(serializers.ModelSerializer):
    dossier = serializers.SerializerMethodField(read_only=True)
    user = AssociationUser(required=True)
    class Meta:
        model = Association
        fields = '__all__'
    def get_dossier(delf, obj):
        dossier = obj.dossier_set.all()
        serializers = DossierSerializer(dossier, many=True)
        return serializers.data

# -------------------------------------------------------------------
class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = dossier
        fields = '__all__'


# -------------------------------------------------------------------

class AlertSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField(read_only=True)
    acceptedBy= serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Alert
        fields = '__all__'


    def get_reviews(delf, obj):
        reviews = obj.review_set.all()
        serializers = ReviewSerializer(reviews, many=True)
        return serializers.data

    def get_sender(self, obj):
        sender = obj.sender
        serializer = Citoyen1(sender, many=False)
        return serializer.data
    def get_acceptedBy(self, obj):
        acceptedBy = obj.acceptedBy
        serializer = Association1(acceptedBy, many=False)
        return serializer.data

# -------------------------------------------------------------------

class EvenementSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField(read_only=True)
    association= serializers.SerializerMethodField(read_only=True)
    alert= serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Evenement
        fields = '__all__'
    def get_members(delf, obj):
        members = obj.members
        serializers = Citoyen1(members, many=True)
        return serializers.data
    def get_association(self, obj):
        association = obj.association
        serializer = Association1(association, many=False)
        return serializer.data
    def get_alert(self, obj):
        alert = obj.alert
        serializer = Alert1(alert, many=False)
        return serializer.data
    def get_reviews(delf, obj):
        reviews = obj.review_set.all()
        serializers = ReviewSerializer(reviews, many=True)
        return serializers.data



class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
    def get_user(self, obj):
        user = obj.user
        serializer = Citoyen1(user, many=False)
        return serializer.data


class EvenementnotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenementnotif
        fields = '__all__'


class AlertnotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alertnotif
        fields = '__all__'
