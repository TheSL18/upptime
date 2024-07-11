from django.shortcuts import render

def condorbs(request):
    return render(request, "condorbs.html")

def ciberseguridad(request):
    return render(request, "ciberseguridad.html")

def minds(request):
    return render(request, "minds.html")

def minos(request):
    return render(request, "minos.html")

def contacto(request):
    return render(request, "contacto.html")

def politicas_de_privacidad(request):
    return render(request, "politicas_de_privacidad.html")