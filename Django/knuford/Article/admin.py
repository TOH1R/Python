from django.contrib import admin
from Article.models import Contact, Blog, Category, Work, Comment, Email, Student

@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'subject')


@admin.register(Blog)
class BlogRegister(admin.ModelAdmin):
    list_display = ("id", 'user',  'category__name')
    list_filter = ("category", )
    
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')    
    
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')    
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category__name', 'description')     
  
       
    
admin.site.register(Comment)    
admin.site.register(Email)    

 
