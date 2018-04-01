from django.contrib import admin
from .models import Blog, BlogType

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "blog_type", "author", "created_time", "lst_update_time")


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name")