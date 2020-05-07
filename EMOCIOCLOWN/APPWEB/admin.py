from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import *

# Register your models here.
"""
admin.site.register(Info)
admin.site.register(Taller)
admin.site.register(Evento)
admin.site.register(Campamento)
admin.site.register(Opiniones)
admin.site.register(Galeria)
admin.site.register(Blog)
admin.site.register(Datos_contacto)
"""

@register(Info)
class MaterialInfoAdmin(admin.ModelAdmin):
    icon_name = 'person'

@register(Taller)
class MaterialContactAdmin(admin.ModelAdmin):
    icon_name = 'title'

@register(Evento)
class MaterialContactAdmin(admin.ModelAdmin):
    icon_name = 'date_range'

@register(Campamento)
class MaterialContactAdmin(admin.ModelAdmin):
    icon_name = 'change_history'

@register(Opiniones)
class MaterialContactAdmin(admin.ModelAdmin):
    icon_name = 'comment'

@register(Galeria)
class MaterialContactAdmin(admin.ModelAdmin):
    icon_name = 'local_see'

@register(Blog)
class MaterialContactAdmin(admin.ModelAdmin):
    icon_name = 'edit'

@register(Datos_contacto)
class MaterialContactAdmin(admin.ModelAdmin):
    icon_name = 'local_post_office'
