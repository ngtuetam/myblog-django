from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse
from blogdtl.models import Post

# Create your views here.

def front_page(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status=Post.ACTIVE).filter(status=Post.ACTIVE)
    return render(request, 'blog/frontpage.html', {'posts': posts})

def about_page(request):
    return render(request, 'blog/aboutpage.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")