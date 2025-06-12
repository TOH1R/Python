from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="blog_image/")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=75)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

