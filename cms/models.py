from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300,null=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=300)
    body = models.TextField(max_length=3000)
    img = models.TextField(max_length=500,default="")
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category,related_name='post_category',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title
