from django.shortcuts import render
from .models import property,category 
from django.core.paginator import Paginator,EmptyPage , PageNotAnInteger

def property_grid(request,**kwargs):
    if kwargs.get('category'):
        all_service = property.objects.filter(category__title=kwargs.get('category'))
    
    else:
        all_service = property.objects.filter(status=True)
    all_services = Paginator(all_service,3) 
    last_page = all_services.num_pages
      
    try:
        page_number = request.GET.get('page')
        all_services = all_services.get_page(page_number)
    except PageNotAnInteger:
        all_services = all_services
    except EmptyPage:
        all_services = all_services
    context = {

        'property' : all_services,
        'category' : category.objects.all()
    }
    return render(request , 'property/property-grid.html', context=context)
def property_single(request ):
    context={
        'category': category .objects.all(),
        'property': property.objects.filter(status=True),  
    }
    
    return render(request , 'property/property-single.html',context=context )