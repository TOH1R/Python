from django.urls import path
from blog.views import blog, blog_detail

urlpatterns = [
    path("", blog, name='blog'),
    path("blog_detail/<int:pk>", blog_detail, name='blog_detail'),
]