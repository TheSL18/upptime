from django.shortcuts import render

def muesart(request):
    return render(request, "muesart.html")

def letras_muesart(request):
    return render(request, "letras_muesart.html")

def nuevos_eventos(request):
    return render(request, "nuevos_eventos.html")

def aviso_de_privacidad(request):
    return render(request, "avido_de_privacidad.html")

def experiencias(request):
    return render(request, "experiencias.html")

def sobre_nosotros(request):
    return render(request, "sobre_nosotros.html")

def sapiens_studios(request):
    return render(request, "sapiens_studios.html")

def tienda_en_lnea(request):
    return render(request, "tienda_en_lnea.html")

def contacto(request):
    return render(request, "contacto.html")

def nuevo_indice(request):
    return render(request, "nuevo_indice.html")

def experiences(request):
    return render(request, "experiences.html")
