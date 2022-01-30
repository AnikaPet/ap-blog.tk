from django.shortcuts import redirect, render
from cms import models
from cms import forms

def category_listing(request):
    '''A view of all categories.'''

    categories = models.Category.objects.all()
    return render(request,'categories/categories_listing.html',{'categories':categories})

def add_category(request):
    '''A view for adding new category.'''

    categories = models.Category.objects.all()
    form = forms.CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request,'categories/add_category.html',{'categories':categories,'form':form})


def edit_category(request,category_id):
    '''A view for editing category.'''

    category = models.Category.objects.get(pk=category_id)
    form = forms.CategoryForm(request.POST or None,instance=category)
    if form.is_valid():
        form.save()

    return render(request,'categories/edit_category.html',{'form':form,'category':category})

def delete_category(request,category_id):
    '''A view for deleting category.'''

    category = models.Category.objects.get(pk=category_id)
    category.delete()
    return redirect('/categories/')

