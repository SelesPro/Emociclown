from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *

# Create your views here.
    
class Index(TemplateView):
    template_name = 'APPWEB/index.html'

    def get_context_data(self,**kwargs):
        context=super(Index, self).get_context_data(**kwargs)
        context['monica'] = Info.objects.get(pk=1)
        context['emocioclown'] = Info.objects.get(pk=2)
        context['talleres'] = Taller.objects.all()[:4]
        context['eventos'] = Evento.objects.all()
        context['campamentos'] = Campamento.objects.all()
        context['opiniones'] = Opiniones.objects.all()
        context['galerias'] = Galeria.objects.all()
        context['blog'] = Blog.objects.all()
        context['contacto'] = Datos_contacto.objects.all()
        return context   

class InfoTaller(ListView):
    model = Taller
    template_name = 'APPWEB/taller.html'

    def get_context_data(self,**kwargs):
        context = super(InfoTaller, self).get_context_data(**kwargs)
        context['taller'] = Taller.objects.get(pk=self.kwargs.get('pk', None))
        return context

class InfoCamp(ListView):
    model = Campamento
    template_name = 'APPWEB/campamento.html'
    context_object_name = 'pro'
    queryset = Campamento.objects.all()

    def get_context_data(self,**kwargs):
        context=super(InfoCamp, self).get_context_data(**kwargs) 
        return context  

class InfoBlog(ListView):
    model = Blog
    template_name = 'APPWEB/blog.html'
    context_object_name = 'blogs'
    queryset = Blog.objects.all()

class SingleBlog(ListView):
    model = Blog
    template_name = 'APPWEB/blog-single.html'

    def get_context_data(self,**kwargs):
        context = super(SingleBlog, self).get_context_data(**kwargs)
        context['singleBlog'] = Blog.objects.get(pk=self.kwargs.get('pk', None))
        return context


