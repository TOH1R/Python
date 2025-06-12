from django.contrib import admin
from instructor.models import Teachers, Category, Best_teacher

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    
    
@admin.register(Teachers)
class CourseAdmin(admin.ModelAdmin):
   list_display = ("id", 'name', 'category')
   list_filter = ("category", )
   
@admin.register(Best_teacher)
class CourseAdmin(admin.ModelAdmin):
   list_display = ("id", 'name', 'category')
   list_filter = ("category", )   
