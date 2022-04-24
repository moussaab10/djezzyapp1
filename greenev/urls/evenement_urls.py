from django.contrib import admin
from django.urls import path,include
from greenev.views import evenement_views as views
from django.urls import reverse

urlpatterns = [
    path('',views.evenementList,name="evenement"),
    path('detail/<str:pk>/', views.getEvenementById, name="evenement_detail"),

]