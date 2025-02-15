from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
    #Create a post : Method 1
    # my_post= Post(
    #     title="My first post",
    #     content="This is my first post. I hope you like it.",
    #     published=True,
    # )
    # #INSERT INTO posts_post (title, content, published, created_at, updated_at) 
    # # VALUES ('My first post', 'This is my first post. I hope you like it.', 1, NOW(), NOW());
    # my_post.save()

    # #Create a post : Method 2
    # my_post= Post.objects.create(
    #     title="My second post",
    #     content="This is my second post. I hope you like it.",
    #     published=True,
    # )

    ## ----!Read a post!---- ##
    #All posts
    # posts=Post.objects.all() #SELECT * FROM posts_post
    # # print(posts) 
    # for obj in posts:
    #     print(obj.title)# printing the title of each post

    # print(posts[0].title) #print the title of the first post
    # print(posts[0].content) #print the content of the first post

    # #Filter posts
    # # posts=Post.objects.filter(title="My first post")
    # posts=Post.object.get(title="My second post") #SELECT * FROM posts_post WHERE title='My first post'
    # print(posts)
    # posts=Post.object.get(id=3) #SELECT * FROM posts_post WHERE id=1
    # print(posts)

    Post.objects.create(
        title="My third post",
        content="This is my third post. I hope you like it.",
        published=False,
    )

    return HttpResponse( "Hello, world. You're at the posts index." )
