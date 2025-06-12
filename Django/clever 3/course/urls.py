from django.urls import path
from course.views import index, courses, index_login, detail, search, regular_page,From_detail 

urlpatterns  = [
    path("", index, name='index'),
    path("courses/", courses, name='courses'),
    path("index_login", index_login, name='index_login'),
    path("detail/<int:pk>", detail, name='detail'),
    path("search/", search, name='search'),
    path("regular_page", regular_page, name='regular_page'),
    path("From_detail/", From_detail, name='From_detail'),
]