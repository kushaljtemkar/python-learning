from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.order_by('pub_date')
    return render(request, "posts/home.html", {'posts': posts})

def detailed_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "posts/detailed_post.html", {"post": post})
