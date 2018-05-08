from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.DO_NOTHING)
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # 二级回复字段  root顶级  parent父级
    root = models.ForeignKey('self', related_name='root_comment', null=True, on_delete=models.DO_NOTHING)
    parent = models.ForeignKey('self', related_name='parent_comment', null=True, on_delete=models.DO_NOTHING)
    reply_to = models.ForeignKey(User, related_name='replies', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text

    def Meta(self):
        ordering = ["-comment_time"]



"""
    开发二级回复思路:
        1、建立model
        2、编写html页面
        3、改进forms.py
        4、改进views.py
        5、测试
"""