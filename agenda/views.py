#from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Contacto


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
    template = get_template("createContact.html")

    context = {
        "titulo": "Crear Contacto"
    }

    return HttpResponse(template.render(context), request)

def editContact(request):
    template = get_template("editContact.html")

    context = {
        "titulo": "Editar Contacto"
    }

    return HttpResponse(template.render(context), request)
