from django.urls import path
from . import views
# from agenda.views import inicio


urlpatterns = [
    path("", views.inicio),
    path("", views.inicio, name = 'base'),
    path('createContact/', views.createContact, name = 'createContact'),
    path('editContact/', views.editContact, name = 'editContact'),
    path('editContact/<str:nombre>/', views.editarContacto, name = 'editContact'),
]

# urlpatterns = [
#     path('', inicio, name = 'base.html')
# ]
