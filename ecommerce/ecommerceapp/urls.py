from ecommerceapp.views import *
from django.urls import path

urlpatterns = [
  
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('checkout/',checkout,name='checkout'),
]
