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
    title = models.CharField(max_length=50, verbose_name='标题')
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    lst_update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改日期')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE, verbose_name='博客类型')
    read_detail = GenericRelation(ReadDetail)

    def __str__(self):
        return "<Blog:%s>" % self.title

    class Meta:
        # 按创建时间倒叙排列
        ordering = ["-created_time"]

