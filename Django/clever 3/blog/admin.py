from django.contrib import admin
from blog.models import Blog, Category, Comment


@admin.register(Blog)
class BlogRegister(admin.ModelAdmin):
    list_display = ("id", 'title', 'category')
    list_filter = ("category", )
    
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')    
    
    
admin.site.register(Comment)