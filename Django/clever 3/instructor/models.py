from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__ (self):
        return self.title

class Teachers(models.Model):
    name = models.CharField(max_length=75)
    image = models.ImageField(upload_to='teachers_image/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


    def __str__ (self):
        return self.name
    
    
class Best_teacher(models.Model):
    name = models.CharField(max_length=75)
    image = models.ImageField(upload_to='best_teachers_image/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField()



    def __str__ (self):
        return self.name
    
