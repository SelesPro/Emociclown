from django.forms import ModelForm
from .models import Contactar

class FormContacto(ModelForm):
    class Meta:
        model = Contactar
        fields = ('nombre', 'email','asunto','mensaje')

