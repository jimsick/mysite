from django.contrib import admin
from .models import Blog, BlogType

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "blog_type", "get_read_num","author", "created_time", "lst_update_time")
    search_fields = ('title',)
    ordering = ('-created_time',)

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name")