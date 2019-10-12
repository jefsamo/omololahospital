from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
    return render(request, 'home.html', {})

def service_screen_view(request):
    return render(request, 'services.html', {})

def about_screen_view(request):
    return render(request, 'about.html', {})

def gallery_screen_view(request):
    return render(request, 'gallery.html', {})