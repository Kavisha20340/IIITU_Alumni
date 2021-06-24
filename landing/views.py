from django.shortcuts import render
from .models import Featured

def landing(request):
    return render(request,'landing/home.html')

def about(request):
    return render(request,'landing/about.html')

def academics(request):
    return render(request,'landing/academics.html')

def contact(request):
    return render(request,'landing/contact.html')

def featured(request):
    context = {
        'featured_alumni' : Featured.objects.all()
    }
    return render(request,'landing/featured_alumni.html',context)