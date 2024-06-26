from django.urls import path
from app1.views import *
app_name='nothing'
urlpatterns=[
    path('lasya/',lasya,name='lasya'),
    path('shree/',shree,name='shree'),

]


