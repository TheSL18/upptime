from django.urls import path
from . import vista

urlpatterns = [
    path("", vista.condorbs, name="condorbs"),
    path("ciberseguridad", vista.ciberseguridad, name="ciberseguridad"),
    path("minds", vista.minds, name="mind"),
    path("minos", vista.minos, name="minos"),
    path("contacto", vista.contacto, name="contacto"),
    path("politicas de privacidad", vista.politicas_de_privacidad, name="politicas_de_privacidad"),
    
]
