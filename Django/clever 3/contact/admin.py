from django.contrib import admin
from contact.models import Contact


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')