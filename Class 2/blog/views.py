from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
 
# def post_list(request):
#     posts=Post.objects.all()
#     result = ''
#     for post in posts:
#         result += post.title + '<br>'
#     return HttpResponse(result)

def post_list(request):
    posts=Post.objects.all()
    return render(request, 'blog/post_list.html')

def post_detail(request,post_id):
    post=Post.objects.get(id=post_id)
    result=f"{post.title}<br>{post.content}"
    return HttpResponse(result)

