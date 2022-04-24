from django.contrib import admin
from django.urls import path,include
from greenev.views import citoyen_views as views
from django.urls import reverse

urlpatterns = [
    path('',views.allCitoyens,name="Citoyens"),
    path('delete/<str:pk>/', views.delteCitoyen, name="citoyen_delete"),
    path('detail/<str:pk>/', views.getCitoyenById, name="citoyen_detail"),
    path('updateState/', views.updateStateCitoyen, name="citoyen_update"),

]
