from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.order_by('pub_date')
    return render(request, "blogtest/home.html", {'posts': posts})

def details(request, post_id):
    post = Post.objects.get(pk = post_id)
    return render(request, "blogtest/post_details.html", {'post': post})
