from django.shortcuts import render
from .models import Agent
from property.models import property,category

def agent_grid(request):
    context={
        'Agent':Agent.objects.all()
    }
    return render(request , 'agent/agents-grid.html',context=context )

def agent_single(request):
    
    context={
      
        'category': property.objects.all(),
        'property': category.objects.filter(statuse=True),  
    }
    return render(request , 'agent/agent-single.html' , context=context )
# Create your views here.
