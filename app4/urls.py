from app4.views import *
from django.urls import path 
app_name='health'

urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
]