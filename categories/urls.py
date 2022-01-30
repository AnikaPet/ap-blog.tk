from django.urls import path
from . import views

urlpatterns = [
    path('',views.category_listing,name='list-categories'),
    path('delete/<int:category_id>',views.delete_category,name='delete-category'),
    path('add-category/',views.add_category,name='add-category'),
    path('edit-category/<int:category_id>',views.edit_category,name='edit-category'),
]
