from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()   
    return render(request, "blog/index.html", context={"posts": posts})

def landing(request):
    return render(request, "blog/landing.html")

def post_detail(request, id):
    p = Post.objects.get(id=id)
    return render(request, "blog/post_detail.html", context={"post": p})
