from django.urls import path
from . import vista


urlpatterns = [
    path('', vista.muesart, name='muesart'),
    path("muesart/", vista.muesart, name="muesart"),
    path("letras-muesart/", vista.letras_muesart, name="letras_muesart"),
    path("nuevos-eventos/", vista.nuevos_eventos, name="nuevos_eventos"),
    path("aviso-de-privacidad/", vista.aviso_de_privacidad, name="aviso_de_privacidad"),
    path("experiencias/", vista.experiencias, name="experiencias"),
    path("sobre-nosotros/", vista.sobre_nosotros, name="sobre_nosotros"),
    path("sapiens-studios/", vista.sapiens_studios, name="sapiens_studios"),
    path("tienda-en-lnea/", vista.tienda_en_lnea, name="tienda_en_lnea"),
    path("contacto/", vista.contacto, name="contacto"),
    path("nuevo-indice", vista.nuevo_indice, name="nuevo_indice"),
    path("experiences", vista.experiences, name="experiences"),
]
