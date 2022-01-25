from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=250)

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING,related_name='user')
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    birth_date = models.DateField(null=True)
    country = models.ForeignKey(Country,related_name='author_country',on_delete=models.DO_NOTHING,null=True)

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=300)
    body = models.TextField(max_length=3000)
    author = models.ForeignKey(Author,related_name='post_author',on_delete=models.DO_NOTHING,null=True)
