
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from book.views import index, detail, update, delete, create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('detail/<int:pk>/', detail, name='detail'),
    path("update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete, name='delete'),
    path("create/", create, name="create"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)