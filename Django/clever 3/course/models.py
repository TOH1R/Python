from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__ (self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=221)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='course_image/')
    price = models.CharField(max_length=30)
    views = models.IntegerField()
    
    def __str__ (self):
        return self.title
    
    
class Register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    site = models.CharField(max_length=50)   
    
    def __str__(self):
        return self.name 
    
    
class Event(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="events_image/")
    price = models.CharField(max_length=30)
    upcoming_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name         