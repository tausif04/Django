from django.db import models

class Post(models.Model): #posts_post
    # id=models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100) # title varchar(100)
    content = models.TextField() # content text
    published = models.BooleanField(default=True) # published boolean0
    created_at = models.DateTimeField(auto_now_add=True , null=True) #created_at TIMESTAMP , input date-time
    updated_ar = models.DateTimeField(auto_now=True , null=True) #updated_at TIMESTAMP , input date-time

    def __str__(self):
        return self.title