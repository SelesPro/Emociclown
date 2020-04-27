
from django.urls import path
from .views import *


urlpatterns = [
    path ('', Index.as_view(),name='index'),
    path('campa/',InfoCamp.as_view(), name = 'campa'),
    
]
