from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="Home"),
    path('register/', views.register , name="Register"),
    path('clubs/', views.ClubChartView.as_view(), name="Club-Chart" )
]