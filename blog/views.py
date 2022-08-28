from django.shortcuts import render,redirect
from .models import Post, Comment
from .forms import ContactForm


def home(request):
    posts = Post.objects.all
    context = {
        'posts': posts
    }
    return render(request,'home.html',context)


def detail(request,slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', slug = post.slug)
    else: 
        form = ContactForm()     
    context = {
        'post': post,
        'form': form
    }
    return render(request,'blog_details.html',context)