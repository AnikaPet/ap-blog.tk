from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=300)
    body = models.TextField(max_length=3000)
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return self.title
