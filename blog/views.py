from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage , PageNotAnInteger
from .models import news
def blog_grid(request,**kwargs):
    if kwargs.get('news'):
        blog = news.objects.filter(title=kwargs.get('news'))
    else :
        blog = news.objects.filter(status=True)

    all = Paginator(blog,3)
    first_page = 1
    last_page = all.num_pages
    try:
        page_number = request.GET.get('page')
        all = all.get_page(page_number)
    except PageNotAnInteger:
        all = all.get_page(1)
    except EmptyPage:
        all = all.get_page(1)
        
    context = {
        'blog' : all,
        'last_page': last_page
            
    }
    
    return render(request , 'blog/blog-grid.html', context=context) 

def blog_single(request,):
  
        # blog_single = news.objects.get(id=id),
        context={
        'blog': blog_single
    }

        return render(request, 'blog/blog-single.html' ,context=context )




