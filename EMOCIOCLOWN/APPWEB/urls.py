
from django.urls import path
from .views import *


urlpatterns = [
    path ('', Index.as_view(),name='index'),
    path ('taller/<int:pk>', InfoTaller.as_view(),name='taller'),
    path('campa/',InfoCamp.as_view(), name = 'campa'),
    
]
