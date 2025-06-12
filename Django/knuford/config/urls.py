from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Article.views import blog_single,index,login_function,register_function, logout_function, contact



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog_single/<int:pk>', blog_single, name='blog_single'),
    path('register/', register_function, name='register'),
    path('login/', login_function, name='login'),
    path('logout/', logout_function, name='logout'),
    path('contact/', contact, name='contact'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)