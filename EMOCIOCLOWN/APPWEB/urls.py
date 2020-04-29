
from django.urls import path
from .views import *



urlpatterns = [
    path ('', Index.as_view(),name='index'),
    path ('taller/<int:pk>', InfoTaller.as_view(),name='taller'), 
    path ('campamento/<int:pk>',InfoCamp.as_view(), name = 'campamento'),
    path ('evento/<int:pk>',InfoEvent.as_view(), name = 'evento'),
    path('blogs/',InfoBlog.as_view(), name = 'blogs'),
    path('singleBlog/<int:pk>',SingleBlog.as_view(), name = 'singleBlog'),
    
    
]
