from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.inventory_detail, name='inventory_detail'),
]