from rest_framework import serializers
from django.contrib.auth.models import User
from cms.models import Category,Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []
        #fields = ['username','password','is_superuser','groups']