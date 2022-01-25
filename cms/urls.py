from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_listing,name='post-list'),
    path('<int:post_id>',views.post_details,name='post-detail'),
    path('search/',views.post_search,name='post-search'),
    path('about-us/',views.about_us,name='about-us'),
    path('delete/<int:post_id>',views.delete_post,name='delete-post'),
    path('add-post/',views.add_post,name='add-post'),
    path('edit-post/<int:post_id>',views.edit_post,name='edit-post')
]
