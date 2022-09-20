from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request,'my_assignment_app/home.html', {'posts':posts})


def latest_post(request):
    post = Post.objects.last()
    return render(request,'my_assignment_app/post.html', {'post':post})
