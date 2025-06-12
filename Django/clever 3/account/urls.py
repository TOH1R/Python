from django.urls import path
from account.views import register_function, login_function, logout_function

urlpatterns = [
    path('register/', register_function, name='register'),
    path('login/', login_function, name='login'),
    path('logout/', logout_function, name='logout'),
]
