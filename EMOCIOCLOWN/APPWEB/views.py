from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.db.models import Q




# Create your views here.
    
class Index(FormView):
    template_name = 'APPWEB/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('appweb:index') 

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

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        asunto = form.cleaned_data['asunto']
        mensaje = "{0} Te ha enviado un mensaje:\n\n {1}".format(nombre, form.cleaned_data['mensaje'])
        send_mail(asunto, mensaje, email, ['laliiosorio@gmail.com'], fail_silently = False)
        
        return super(Index, self).form_valid(form)
     

class InfoTaller(ListView):
    model = Taller
    template_name = 'APPWEB/taller.html'

    def get_context_data(self,**kwargs):
        context = super(InfoTaller, self).get_context_data(**kwargs)
        context['contactoInfo']= Contactar.objects.all()   #[0] para que era? si no funciona 
        context['taller'] = Taller.objects.get(pk=self.kwargs.get('pk', None))
        return context

class InfoCamp(ListView):
    model = Campamento
    template_name = 'APPWEB/campamento.html'

    def get_context_data(self,**kwargs):
        context=super(InfoCamp, self).get_context_data(**kwargs) 
        context['campamento'] = Campamento.objects.get(pk=self.kwargs.get('pk', None))
        return context  

class InfoEvent(ListView):
    model = Evento
    template_name = 'APPWEB/evento.html'

    def get_context_data(self,**kwargs):
        context=super(InfoEvent, self).get_context_data(**kwargs) 
        context['evento'] = Evento.objects.get(pk=self.kwargs.get('pk', None))
        return context 


class InfoBlog(ListView):
    model = Blog
    template_name = 'APPWEB/blog.html'
    context_object_name = 'blogs'
    paginate_by = 3
    queryset = Blog.objects.all()

class SingleBlog(ListView):
    model = Blog
    template_name = 'APPWEB/blog-single.html'

    def get_context_data(self,**kwargs):
        context = super(SingleBlog, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('pk', None)
        context['singleBlog'] = Blog.objects.filter(id=parametro)
        return context

             
