from django import forms
# from django.forms import ModelForm
from .models import Contacto


# from PIL import Image
# from django.core.files.uploadedfile import SimpleUploadedFile

from django.core.files.uploadedfile import SimpleUploadedFile

class ContactoForm(forms.ModelForm):
  class Meta:
    model = Contacto
    fields = '__all__'





# class ContactoForm(ModelForm):
#   class Meta:
#     model = Contacto
#     fields = '__all__'
