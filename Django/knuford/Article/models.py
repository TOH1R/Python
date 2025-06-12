from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=221)
    message = models.TextField()
    
    def __str__(self):
        return self.name   
 
class Email(models.Model):
    email = models.EmailField(unique=True)    
    
    def __str__(self):
        return self.email

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='image_blog/')
    category = models.ManyToManyField(Category)
    
    
    def __str__(self):
        return self.title
    
class Work(models.Model):
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='image_work/')
    description = models.TextField()
    category = models.ManyToManyField(Category)  
    create_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name  
   
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=75)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    create_date = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=221)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='image_student/')
    description = models.TextField()
    
    def __str__(self):
        return self.name
