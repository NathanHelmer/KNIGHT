from django.urls import path
from . import views

urlpatterns = [
    path('nmap-scans/', views.nmap_scans, name='nmap'),
]