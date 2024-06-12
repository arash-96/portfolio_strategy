from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update-trade/<str:pk>/', views.update_trade, name='update-trade'),
]