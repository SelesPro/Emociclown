from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView
from .models import *

from APPWEB.forms import FormContacto

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
        context['FormContacto'] = FormContacto

        return context 

    def contactomail(request):
        if request.method == 'POST':
            formulario = FormContacto(request.POST)
            if formulario.is_valid():
                asunto = 'Asunto de contacto'
                mensaje = formulario.cleaned_data['mensaje'] 
                mail = EmailMessage(asunto, mensaje, to=['email@gmail.com'])
                mail.send()
            return HttpResponseRedirect('/') 
        else:
            formulario = FormContacto() 
        return render_to_response('contacto_mail.html', {'formulario':formulario}, context_instance=RequestContext(request))


class InfoTaller(ListView):
    model = Taller
    template_name = 'APPWEB/taller.html'

    def get_context_data(self,**kwargs):
        context = super(InfoTaller, self).get_context_data(**kwargs)
        context['contactoInfo']= Contactar.objects.all()[0]
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
    queryset = Blog.objects.all()

class SingleBlog(ListView):
    model = Blog
    template_name = 'APPWEB/blog-single.html'

    def get_context_data(self,**kwargs):
        context = super(SingleBlog, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('pk', None)
        context['singleBlog'] = Blog.objects.filter(id=parametro)
        return context

             
