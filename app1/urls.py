from django.urls import path
from app1.views import *
app_name='aa'
urlpatterns=[
    path('mass/',mass,name='mass')
]