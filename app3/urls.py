from django.urls import path
from app3.views import *
app_name='nothing'
urlpatterns=[
    path('Vrindha/',Vrindha,name='Vrindha'),
    path('Vandhana/',Vandhana,name='Vandhana'),
    
]