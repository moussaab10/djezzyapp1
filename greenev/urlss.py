
from django.contrib import admin
from django.urls import path,include
from . import viewss
urlpatterns = [
    path('',viewss.apiOverview,name="api.piOverview"),
    path('citoyen/',viewss.citoyenList,name="citoyenList"),
]