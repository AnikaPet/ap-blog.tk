from django.db.models.fields import mixins
from rest_framework import mixins
from rest_framework import viewsets

from django.contrib.auth.models import User
from cms.models import Category,Post
from .serializers import CategorySerializer, PostSerializer, UserSerializer

class CategoryViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# mixins.CreateModelMixin,mixins.UpdateModelMixin
class PostViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                    mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    search_fields = ['title']

class UserViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
