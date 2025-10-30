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

    # #----Filter posts-----#   
    # # posts=Post.objects.filter(title="My first post")
    # posts=Post.object.get(title="My second post") #SELECT * FROM posts_post WHERE title='My first post'
    # print(posts)
    # posts=Post.object.get(id=3) #SELECT * FROM posts_post WHERE id=1
    # print(posts)

    # Post.objects.create(
    #     title="My third post",
    #     content="This is my third post. I hope you like it.",
    #     published=False,
    # )
    # #LookUp
    # posts=Post.objects.filter(title__contains="My") #SELECT * FROM posts_post WHERE title LIKE '%My%'
    # posts=Post.objects.filter(title__icontains="My") #case-insensitive
    # print(posts)
    # posts=Post.objects.filter(title__startswith="My") #SELECT * FROM posts_post WHERE title LIKE 'My%'
    # print(posts)    
    # posts=Post.objects.filter(title__endswith="post") #SELECT * FROM posts_post WHERE title LIKE '%post'
    # print(posts)
    # posts=Post.objects.filter(title__iendswith="POST") #case-insensitive
    # posts=Post.objects.filter(id__in=[1,2,3]) #SELECT * FROM posts_post WHERE id IN (1,2,3)
    # print(posts)
    # posts=Post.objects.filter(id__gt=1) #SELECT * FROM posts_post WHERE id>1
    # print(posts)
    # posts=Post.objects.filter(id__gte=1) #SELECT * FROM posts_post WHERE id>=1
    # print(posts)
    # posts=Post.objects.filter(id__lt=3) #SELECT * FROM posts_post WHERE id<3
    # print(posts)        
    # posts=Post.objects.filter(id__lte=3) #SELECT * FROM posts_post WHERE id<=3
    # print(posts)
    # posts=Post.objects.filter(id__range=[1,3]) #SELECT * FROM posts_post WHERE id BETWEEN 1 AND 3
    # print(posts)

    
    # Update
    posts = Post.objects.filter(published=True)
    # for post in posts:   # Loop is the worst way to update multiple records
    #     post.published = False
    #     post.save()
    posts.update(published=False)  # This is the best way to update multiple records.
                                      #It is not  for single record update.

    # Delete
    # posts = Post.objects.all()
    # for post in posts:
    #     post.delete()
    
    # Or we can do it in one line
    # Post.objects.all().delete()
    Post.objects.all().exclude(published=False) #SELECT * FROM posts_post WHERE published=1
    Post.objects.all().filter(published=False).delete() #DELETE FROM posts_post WHERE published=0

    return HttpResponse( "Hello, world. You're at the posts index." )
