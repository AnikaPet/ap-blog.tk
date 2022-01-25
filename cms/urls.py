from django.urls import path
from . import views

urlpatterns = [
    path('posts/',views.post_listing,name='post-list'),
    path('posts/<int:post_id>',views.post_details,name='post-detail'),
    path('posts/search/',views.post_search,name='post-search')
    
]