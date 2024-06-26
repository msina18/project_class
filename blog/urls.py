from django.urls import path
from django.contrib import admin
from .views import blog_single , blog_grid
app_name = 'blog'
urlpatterns = [
    path('' , blog_grid , name = 'blog-grid'),
    path('blog-single/' , blog_single , name='blog-single'),
    path('blog-single/<int:id>' , blog_single , name='blog-single'),
    path('blog-single/<int:id>' , blog_single , name='list_by_blog_single'),
]
