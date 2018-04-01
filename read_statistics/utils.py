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


"""计算7天内每天的阅读数"""
def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    read_nums_dates = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)  # 每前一天
        readDetail = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = readDetail.aggregate(read_num_sum=Sum('read_num'))  # 聚合统计一天内所有的阅读数
        read_nums.append(result["read_num_sum"] or 0)
        read_nums_dates.append(date.strftime("%m/%d"))
    return read_nums_dates, read_nums