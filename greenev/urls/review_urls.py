from django.contrib import admin
from django.urls import path,include
from greenev.views import review_views as views
from django.urls import reverse

urlpatterns = [
    path('',views.reviewList,name="reviewList"),
]