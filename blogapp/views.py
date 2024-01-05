from django.shortcuts import render
from .models import Blog
# Create your views here.

def index(request):
    featured_blog = Blog.objects.get(featured=True)
    blogs = Blog.objects.filter(featured=False)
    context = {"blogs":blogs, "f_blog": featured_blog}
    return render(request, "blogapp/index.html", context)

def detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {'blog': blog}
    return render(request, "blogapp/detail.html", context)