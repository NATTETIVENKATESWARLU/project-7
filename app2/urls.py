from django.urls import path
from app2.views import *
app_name='bb'
urlpatterns=[
    path('venkey/',venkey,name='venkey')
]