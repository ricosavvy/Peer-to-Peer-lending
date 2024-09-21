# backend/app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.get_prediction, name='predict'),
    path('graph/', views.get_graph, name='graph'),
]
