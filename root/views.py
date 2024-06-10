from django.shortcuts import render
from property.models import property
from .models import service,Testimonials
from agent.models import Agent
from blog.models import news

# from .models import service

def home (request):
    context={
        'news':news.objects.all(),
        'agent':Agent.objects.all()[:2],
        'Testimonials':Testimonials.objects.filter(status=True),
        'service':service.objects.filter(status=True),
        'property':property.objects.filter(status=True)[:2],
    }
    return render(request,'root/index.html',context=context)

def about (request):
    context={
        'agent':Agent.objects.all(),
    }
    return render(request,'root/about.html',context=context)

def contact(request):
    return render(request,'root/contact.html')

# ****************************
def property_grid(request):
    return render(request,'root/property-grid')

# Create your views here.
