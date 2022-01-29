from django.shortcuts import render
from .models import Category, Post
from .forms import PostForm

def about_us(request):
    '''A view of about us page.'''

    return render(request,'about_us.html')

def post_listing(request):
    '''A view of all blog posts.'''
    categories = Category.objects.all()
    posts = Post.objects.all()  
    return render(request,'posts/post_listing.html',{'posts':posts,'categories':categories})

def post_details(request,post_id):
    '''A view of details of blog post.'''

    post = Post.objects.get(pk=post_id) 
    return render(request,'posts/post_detail.html',{'post':post})

def post_search(request):
    '''A view of posts searched by title.'''

    queried_post = request.GET['q']
    posts = None

    posts = Post.objects.filter(title__contains = queried_post)

    if not posts:
        queried_post_exists = False
    else:
        queried_post_exists = True
    
    return render(request,'posts/post_searched.html',{'posts':posts,'results':queried_post_exists})

def delete_post(request,post_id):
    '''A view for deleting post.'''

    post = Post.objects.get(pk=post_id)
    post.delete()
    return render(request,'posts/delete_post.html',{'post':post})

def add_post(request):
    '''A view for adding new post.'''

    posts = Post.objects.all()
    form = PostForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form = PostForm()

    return render(request,'posts/add_post.html',{'posts':posts,'form':form})

def edit_post(request,post_id):
    '''A view for editing post.'''

    posts = Post.objects.all()
    instance = Post.objects.get(pk=post_id)
    form = PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()

    return render(request,'posts/edit_post.html',{'form':form,'posts':posts})
