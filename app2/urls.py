from django.urls import path
from app2.views import *
app_name='nothing'
urlpatterns=[
    path('yash/',yash,name='yash'),
    path('Akarsh/',Akarsh,name='Akarsh'),

]
