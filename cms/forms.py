from django import forms
from django.forms import fields

from .models import Category, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            'title',
            'body',
            'img',
            'category'
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = {
            'name',
            'description'
        }