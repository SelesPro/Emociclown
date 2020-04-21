from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.
    
class Index(TemplateView):
    template_name = 'APPWEB/index.html'

    def get_context_data(self,**kwargs):
        context=super(Index, self).get_context_data(**kwargs)
        context['monica'] = Info.objects.get(pk=1)
        context['emocioclown'] = Info.objects.get(pk=2)
        context['talleres'] = Taller.objects.all()
        context['eventos'] = Evento.objects.all()
        context['campamentos'] = Campamento.objects.all()
        context['opinion'] = Opiniones.objects.all()
        context['galerias'] = Galeria.objects.all()
        context['blog'] = Blog.objects.all()
        context['contacto'] = Contactar.objects.all()
        return context    


