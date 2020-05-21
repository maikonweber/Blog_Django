# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Post

# Create your views here.

def home(request):
    post = Post.objects.all()
    return render (request, "home.html", {"posts": post })

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "post.html", {"post":post})