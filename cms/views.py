from django.shortcuts import render
from .models import Post

def about_us(request):
    return render(request,'about_us.html')

def post_listing(request):
    '''A view of all blog posts.'''
    posts = Post.objects.all()  
    return render(request,'posts/post_listing.html',{'posts':posts})

def post_details(request,post_id):  #dodajemo parametar koji je proslijedjen kroz url
    '''A view of details of blog post.'''
    post = Post.objects.get(pk=post_id) 
    return render(request,'posts/post_detail.html',{'post':post})

def post_search(request):
    #imamo GET parametar ? ime par = vrijednost (razmaci su ili + ili %)
    queried_post = request.GET['q']
    post = None
    try:
        post = Post.objects.get(title = queried_post)
        queried_post_exists = True
    except:
        queried_post_exists = False
    return render(request,'posts/post_searched.html',{'post':post,'results':queried_post_exists})

def delete_post(request,post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return render(request,'posts/delete_post.html',{'post':post})
    