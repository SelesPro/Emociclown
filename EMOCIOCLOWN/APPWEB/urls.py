
from django.urls import path
from .views import *
from APPWEB import views


urlpatterns = [
    path ('', Index.as_view(),name='index'),
    path ('taller/<int:pk>', InfoTaller.as_view(),name='taller'),
    path('campa/',InfoCamp.as_view(), name = 'campa'),
    path('blogs/',InfoBlog.as_view(), name = 'blogs'),
    path('singleBlog/<int:pk>',SingleBlog.as_view(), name = 'singleBlog'),
    
]
