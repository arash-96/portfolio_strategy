from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update-trade/<str:pk>/', views.new_trade, name='update-trade'),
]