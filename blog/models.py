from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadDetail, ReadNumExpandMethod

class BlogType(models.Model):
    type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.type_name


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True)
    lst_update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    read_detail = GenericRelation(ReadDetail)
    def __str__(self):
        return "<Blog:%s>" % self.title
    # 按创建时间倒叙排列
    class Meta:
        ordering = ["-created_time"]

