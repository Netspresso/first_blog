from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def blog_main_page(request):
    return render(request, 'blog.html')