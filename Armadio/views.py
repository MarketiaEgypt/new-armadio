from django.shortcuts import render

# Create your views here.

from blog.models import Post


def home(request):
    posts = Post.objects.all()[:3]
    return render(request, 'home/index.html', {
        'posts': posts,
    })


def sitemap(request):
    return render(request, 'home/sitemap.xml')


def robots(request):
    return render(request, 'home/robots.txt')