from django.contrib import admin
from django.urls import path,include
from greenev.views import notification_views as views
from django.urls import reverse

urlpatterns = [
    path('alert-notification-list/',views.alertNotifList,name="alertNotifList"),
    path('evenement-notif-list/',views.evenementNotifList,name="evenementNotifList"),
]
