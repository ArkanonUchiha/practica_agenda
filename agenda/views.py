from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Contacto

from .forms import ContactoForm
# from .forms import ContactoForm


def inicio(request):
    template = get_template("base.html")
    contactos = Contacto.objects.all()

    print(contactos)

    context = {
        "contactos": contactos,
        "titulo": "Inicio"
    }

    return HttpResponse(template.render(context), request)





def createContact(request):
    # template = get_template("createContact.html")
    # context = {
    #     "titulo": "Crear Contacto"
    # }

    if request.method == 'GET':
        form = ContactoForm()
        context = {
            'form': form
        }
    else:
        form = ContactoForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('editContact')

    # return HttpResponse(template.render(context), request)
    return render(request, 'createContact.html', context)





def editContact(request):
    template = get_template("editContact.html")

    context = {
        "titulo": "Editar Contacto"
    }

    return HttpResponse(template.render(context), request)





def editarContacto(request, nombre):
    contacto = Contacto.objects.get(nombre = nombre)
    if request.method == 'GET':
        form = ContactoForm(instance = contacto)
        context = {
            'form': form
        }
    return render(request, 'editContact.html', context)




