from django.shortcuts import render_to_response
from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import (get_seven_days_read_data,
                                   get_yesterday_hot_read_data,
                                   get_today_hot_read_data,
                                   get_7_days_hot_data)
from blog.models import Blog
from django.utils import timezone
from django.db.models import Sum
import datetime


# def savecache(func, name, blog_content_type):
#     result = cache.get(name)
#     if not result:




def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    read_nums_dates, read_nums = get_seven_days_read_data(blog_content_type)
    yesterday_hot_data = get_yesterday_hot_read_data(blog_content_type)
    today_hot_data = get_today_hot_read_data(blog_content_type)
    week_days_hot_data = get_7_days_hot_data(blog_content_type)
    context = {
        "read_nums": read_nums,
        "read_nums_dates": read_nums_dates,
        "yesterday_hot_data": yesterday_hot_data,
        "today_hot_data": today_hot_data,
        "week_days_hot_data": week_days_hot_data,
    }
    return render_to_response('home.html', context)
