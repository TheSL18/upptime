from django.urls import path
from . import vista

urlpatterns = [
    path('', vista.globalists, name="globalists"),
    path("planes-comerciales/", vista.planes_comerciales, name="planes_comerciales"),
    path("faq/", vista.faq, name="faq"),
    path("contacto/", vista.contacto, name="contacto"),
    path("long-in/", vista.long_in, name="long_in"),
]
