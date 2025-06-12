from django.urls import path
from instructor.views import instructors

urlpatterns = [
    path("", instructors, name='instructors'),
 
]