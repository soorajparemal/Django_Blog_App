from django.shortcuts import render_to_response
from .models import Post
# Create your views here.

def tagpage(request,tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response('tagpage.html',{'posts': posts,'tag': tag})

def mainpage(request):
    return render_to_response('mainpage.html')