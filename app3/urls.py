from app3.views import *
from django.urls import path
app_name='positivity'

urlpatterns=[
    path('virat/',virat,name='virat'),
]