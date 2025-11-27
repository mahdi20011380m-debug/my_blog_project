from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm 
from .forms import CommentForm

def index(request):
    posts = Post.objects.all()   
    return render(request, "blog/index.html", context={"posts": posts})

def landing(request):
    return render(request, "blog/landing.html")



def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.post = post
            c.save()
            return redirect('post_detail', id=id)
    else:
        form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form
    })

def creat_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()

    return render(request, 'blog/creat_post.html', {'form': form})


 

def regsister_client(request):
    if request.metod=="GET":
        return render(request,"accounts/register.html",context={})
    elif request.method=="POST":
        pass

    
def comment_crat(request):
    return render ()