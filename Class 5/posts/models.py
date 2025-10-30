from django.db import models

class Post(models.Model): #posts_post
    # id field is created automatically as primary key
    title = models.CharField(max_length=200) #posts_post_title
    content = models.TextField() #posts_post_content
    published = models.BooleanField(default=False) #posts_post_published
    created_at = models.DateTimeField(auto_now_add=True) #posts_post_created_at
    updated_at = models.DateTimeField(auto_now=True, null=True) #posts_post_updated_at
    tags = models.ManyToManyField('Tag', blank=True) #posts_post_tags

    def __str__(self):
        return self.title
# Create your models here.

class PostExtraInfo(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE) #posts_postextrainfo_post
    rating = models.FloatField(default=0.0) #posts_postextrainfo_rating
    def __str__(self):
        return f"Extra info for {self.post.title}"
    

class Comment(models.Model):
    content = models.TextField() #posts_comment_content
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #posts_comment_post

    def __str__(self):
        return f"Comment on {self.post.title}"

class Tag(models.Model):
    name = models.CharField(max_length=50) #posts_tag_name

    def __str__(self):
        return self.name
