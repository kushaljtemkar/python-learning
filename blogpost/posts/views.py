from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, "posts/home.html", {'posts':posts})

def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "posts/post_details.html", {'post':post})
