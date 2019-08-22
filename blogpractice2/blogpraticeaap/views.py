from django.shortcuts import render
from .models import Post
from blogpractice2 import urls

def home(request):
    posts = Post.objects.order_by('pub_date')
    return render(request, "blogpraticeaap/home.html", {'posts': posts})

def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)    
    return render(request, "blogpraticeaap/post_details.html", {'post': post})
