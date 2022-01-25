from django.contrib import admin
from django.urls import path,include

from cms import views

urlpatterns = [

    path('',views.about_us),
    path('admin/', admin.site.urls),
    path('blog/',include('cms.urls')),
    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
]
