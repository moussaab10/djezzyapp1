from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings
from django.utils.timezone import now

# +++

class User(AbstractUser):
    Grade = (
        ("AUCUN", "aucun"),
        ("SUPERADMAIN", "superadmin"),
        ("ANALYST", "analyste"),
        ("EDITEURE", "editeur"),
    )

    GradeState = models.CharField(
        max_length=20, choices=Grade, default="AUCUN")
    image = models.ImageField(null=True, blank=True,default='/placeholder.png')
    online=models.BooleanField(default=False)

    def __str__(self):
        return self.username



class Citoyen(models.Model):
    STATE = (
        ("ACTIVE", "active"),
        ("BLOCKED", "blocked"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    number = models.CharField(
        max_length=200, null=False, blank=False, unique=True)
    evenementState = models.BooleanField(default=False)
    CitezenState = models.BooleanField(default=True)
    # CitezenState = models.CharField(
        # max_length=20, choices=STATE, default="ACTIVE")
    wilaya = models.CharField(max_length=50, null=False)
    commune = models.CharField(max_length=50, null=False)
    ville = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    nbAlert=models.IntegerField(null=True,blank=True)
    nbEvenem=models.IntegerField(null=True,blank=True)
    # _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.user.username




class Association(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  primary_key=True)
    name = models.CharField(max_length=200)
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    number = models.CharField(max_length=200)
    authNumber = models.CharField(max_length=200)
    wilaya = models.CharField(max_length=50, null=False)
    commune = models.CharField(max_length=50, null=False)
    ville = models.CharField(max_length=50, null=False)
    dateCreat = models.DateTimeField(default=now, null=False)
    address = models.CharField(max_length=50, null=False)
    associationState = models.BooleanField(default=False)
    dossiertState = models.BooleanField(default=False)
    nbEvenem=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.name)

class dossier(models.Model):
    association = models.ForeignKey(Association, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True,default='/placeholder.png')
    def __str__(self):
        return str(self.association)


# # member




class Alert(models.Model):
    STATE = (
        ("NOTYET", "not yet "),
        ("Accepted", "accepted"),
    )
    STATE2 = (
        ("CANCELLED", " cancelled"),
        ("ACTIVE", "active"),
    )
    # alertState = models.CharField(max_length=20, choices=STATE2, default="ACTIVE")
    # acceptedState = models.CharField(max_length=20, choices=STATE, default="NOTYET")
    alertState = models.BooleanField(default=True)
    acceptedState = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    # citoyen
    cancelledReson = models.TextField(null=True, blank=True)
    sender = models.ForeignKey(Citoyen, on_delete=models.SET_NULL, null=True)
    discription = models.TextField(null=True,blank=True)
    wilaya = models.CharField(max_length=50, null=False,default='')
    commune = models.CharField(max_length=50, null=False,default='')
    ville = models.CharField(max_length=50, null=True,blank=True)
    # association
    acceptedBy = models.ForeignKey(Association, on_delete=models.SET_NULL, null=True,blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    state = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.id)

class Evenement(models.Model):
    STATE = (
        ("DISPO", "disponile"),
        ("NOTDISPO", "not disponible"),
        ("INPROGRESS", "in progress"),
        ("REPORTED", "reported"),
        ("CANCELLED", "cancelled"),
        ("FINISHED", "finished"),
    )
    reson = models.TextField(null=True, blank=True)

    EvenementState = models.CharField(max_length=20, choices=STATE, default="DISPO")
    association = models.ForeignKey(Association, on_delete=models.SET_NULL, null=True)
    alert = models.ForeignKey(Alert, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200, null=True, blank=True, unique=True)
    date = models.DateField(auto_now_add=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    dateUpdate = models.DateField(auto_now_add=False, null=True, blank=True)
    dateEnd = models.DateField(auto_now_add=False, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True,default='/placeholder1.png')
    image2 = models.ImageField(null=True, blank=True,default='/placeholder2.png')
    members = models.ManyToManyField(Citoyen)

    def __str__(self):
        return self.name

class Review(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Citoyen, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateField(auto_now_add=True)
    # _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.evenement)

class Notification(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    state = models.BooleanField(verbose_name='deja Lu', default=False)
    # _id = models.AutoField(primary_key=True, editable=False)


class Evenementnotif(Notification):
    evenement = models.OneToOneField(
        Evenement, on_delete=models.CASCADE, null=True)
    # date = models.DateTimeField(auto_now_add=False)
    # state = models.BooleanField(default=False)

    def __str__(self):
        return str(self.evenement)

#
class Alertnotif(Notification):
    alert = models.OneToOneField(Alert, on_delete=models.CASCADE)
    # date = models.DateTimeField(auto_now_add=False)
    # state = models.BooleanField(default=False)

    def __str__(self):
        return str(self.alert)
