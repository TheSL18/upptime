from django.urls import path
from . import vista

urlpatterns = [
    path('', vista.cb_america, name='cb_america'),
    path('cb_america_web/', vista.cb_america, name='cb_america'),
    path("products-services/", vista.products_services, name="products_services"),
    path("about-us/", vista.about_us, name="about_us"),
    path("global-lists/", vista.global_lists, name="global_lists"), 
]