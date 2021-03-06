import re
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from cms import models

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def ProfileView(request):
    model = models.Post
    posts = model.objects.all()

    return render(request,'userprofile.html',{'posts':posts})
