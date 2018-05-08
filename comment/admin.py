from django.contrib import admin
from .models import Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "text", "comment_time", "root", "parent", "reply_to")
    ordering = ('-comment_time',)