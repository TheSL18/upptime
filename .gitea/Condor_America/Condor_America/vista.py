from django.shortcuts import render

def cb_america(request):
    return render(request, "cb_america.html")

def products_services(request):
    return render(request, "products_services.html")

def global_lists(request):
    return render(request, "global_lists.html")

def about_us(request):
    return render(request, "about_us.html")
