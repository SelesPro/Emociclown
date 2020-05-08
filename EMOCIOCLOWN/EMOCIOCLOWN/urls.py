"""EMOCIOCLOWN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from APPWEB import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('', include(('APPWEB.urls','appweb'))),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 
# RUTA VALIDA DENTRO DE APLICACION


#PERSONALIZACION COLOR DJANGO-ADMIN-MATERIAL

"""
admin.site_header = _('admin')

site.site_title = _('Emocioclown')
site.favicon = staticfiles('favicon.png')
site.main_bg_color = 'green'
site.main_hover_color = 'yellow'
site.profile_picture = staticfiles('profile-background.jpeg')
site.profile_bg = staticfiles('profile-background.jpeg')
site.login_logo = staticfiles('profile-background.jpeg')
site.logout_bg = staticfiles('profile-background.jpeg')
"""