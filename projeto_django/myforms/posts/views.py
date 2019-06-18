from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'list_posts.html', {'posts': posts.order_by('-data_published')})


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.editable = True
            model_instance.data_published = 'now'
            model_instance.save()
            return redirect('list_posts')
    else:
        form = PostForm()
        return render(request, 'add_book.html', {'form': form})


def edite(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            post.title = model_instance.title
            post.text = model_instance.text
            post.tag = model_instance.tag
            post.data_published = 'now'
            post.save()
            return redirect('list_posts')
    else:
        form = PostForm()
        return render(request, 'edite.html', {'post': post, 'form': form})
