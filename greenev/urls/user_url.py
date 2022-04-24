from django.urls import path
from greenev.views.user_view import MyTokenObtainPairView,getUserProfile,addAdmin
from greenev.views import user_view as views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns=[
path('', views.allUsers, name='all_users'),
path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('add/', views.addAdmin, name='add_admin'),
path('profil/', views.getUserProfile, name='profile'),
path('delete/<str:pk>/', views.delteUsers, name="users_delete"),
path('detail/<str:pk>/', views.getUserById, name="users_detail"),
path('update/', views.updateUser, name="users_detail"),


]
