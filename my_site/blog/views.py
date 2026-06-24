from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')

def post_list(request):
    return render(request, 'blog/list.html')

def get_post(request, id):
    return render(request, 'blog/post.html', context={'id': id})

def get_post_comments(request, id):
    return render(request, 'blog/comments.html', context={'id': id})
