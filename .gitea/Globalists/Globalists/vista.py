from django.shortcuts import render

def globalists(request):
    return render(request, "globalists.html")

def planes_comerciales(request):
    return render(request, "planes_comerciales.html")

def faq(request):
    return render(request, "faq.html")

def contacto(request):
    return render(request, "contacto.html")

def long_in(request):
    return render(request, "long_in.html")

