from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def say_hello(request):
    return HttpResponse('Hello Django!')

def say_hi(request):
    return render(request, 'hi.html', {'name': 'Christian Buizon'})

def blog_list(request):
    post = Post.objects.all()
    context = {
        'blog_list': post
    }
    return render(request, 'blog_list.html', context)

def blog_detail(request, id):
    each_post = Post.objects.get(id = id)
    context = {
        'blog_detail': each_post
    }
    return render(request, 'blog_details.html', context)