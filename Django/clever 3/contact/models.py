from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField(unique=True)
    message = models.TextField()
    
    def __str__(self):
        return self.name   