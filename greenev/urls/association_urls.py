from django.contrib import admin
from django.urls import path,include
from greenev.views import association_views as views
from django.urls import reverse

urlpatterns = [
    path('',views.associationList,name="association"),
    path('delete/<str:pk>/', views.delteAssociation, name="association_delete"),
    path('detail/<str:pk>/', views.getAssociationById, name="association_detail"),
    path('updateState/', views.updateStateAssociation, name="association_update"),

]