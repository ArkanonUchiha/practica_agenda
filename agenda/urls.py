from django.urls import path
from . import views
# from agenda.views import inicio


urlpatterns = [
    path("", views.inicio),
    path('createContact/', views.createContact, name = 'createContact'),
    path('editContact/', views.editContact, name = 'editContact'),
]

# urlpatterns = [
#     path('', inicio, name = 'base.html')
# ]
