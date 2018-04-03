from blog.models import Blog
from read_statistics.models import ReadNum, ReadDetail
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
import datetime


def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)
    if not request.COOKIES.get(key):
        readNum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readNum.read_num += 1
        readNum.save()


        date = timezone.now().date()
        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num += 1
        readDetail.save()
    return key


def get_seven_days_read_data(content_type):
    """计算7天内每天的阅读数"""
    today = timezone.now().date()
    read_nums = []
    read_nums_dates = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)  # 每前一天
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))  # 聚合统计一天内所有的阅读数
        read_nums.append(result["read_num_sum"] or 0)
        read_nums_dates.append(date.strftime("%m/%d"))
    return read_nums_dates, read_nums


def get_today_hot_read_data(content_type):
    """计算今日热门阅读数"""
    today = timezone.now().date()
    read_details = ReadDetail.objects \
                             .filter(content_type=content_type, date=today) \
                             .order_by("-read_num")
    return read_details[:7]


def get_yesterday_hot_read_data(content_type):
    """计算昨日热门阅读数"""
    yesterday = timezone.now().date() - datetime.timedelta(days=1)
    read_details = ReadDetail.objects \
                             .filter(content_type=content_type, date=yesterday) \
                             .order_by("-read_num")
    return read_details[:7]


def get_7_days_hot_data(content_type):
    """前一周热门点击文章"""
    date = timezone.now().date() - datetime.timedelta(days=7)
    blogs = Blog.objects \
                .filter(read_detail__content_type=content_type, read_detail__date__gt=date) \
                .values("id", "title") \
                .annotate(read_num_sum=Sum("read_detail__read_num")) \
                .order_by("-read_num_sum")
    return blogs


