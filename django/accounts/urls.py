from django.urls import path
from rest_framework import urlpatterns 
from rest_framework.urlpatterns import format_suffix_patterns

from accounts import views
from django.urls import include, path
from rest_framework import routers

urlpatterns= [
    path('profile/', views.ProfileView.as_view()),
    path('api/auth', views.CustomAuthToken.as_view()),
     path('register/', views.RegisterView.as_view(), name='auth_register'),

]

urlpatterns= format_suffix_patterns(urlpatterns)


