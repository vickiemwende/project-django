from django.shortcuts import render

def indexpage(request):
    return render(request, 'index.html')
def homepage(request):
    return render(request, 'home.html')
def aboutpage(request):
    return render(request, 'about.html')
def servicespage(request):
    return render(request, 'services.html')
def contactpage(request):
    return render(request, 'contact.html')
def productpage(request):
    return render(request, 'products.html')
def blogpage(request):
    return render(request, 'blog.html')