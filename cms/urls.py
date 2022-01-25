from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_listing,name='post-list'),
    path('<int:post_id>',views.post_details,name='post-detail'),
    path('search/',views.post_search,name='post-search'),
    path('about-us/',views.about_us,name='about-us')
]