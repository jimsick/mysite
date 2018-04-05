from django.shortcuts import render_to_response, render, redirect, reverse
from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.db.models import Sum
import datetime
from blog.models import Blog
from read_statistics.utils import (get_seven_days_read_data,
                                   get_yesterday_hot_read_data,
                                   get_today_hot_read_data,
                                   get_7_days_hot_data)



def savecache(func, name, blog_content_type, time=60):
    """
        将数据保存到cache中
        func  方法名
        name  cache中对应的key
        blog_content_type
    """
    result = cache.get(name)
    if not result:
        result = func(blog_content_type)
        cache.set(name, result, time)
    return result


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)  # blog类型
    read_nums_dates, read_nums = get_seven_days_read_data(blog_content_type)  # 一周每天阅读量
    yesterday_hot_data = get_yesterday_hot_read_data(blog_content_type)  # 昨日热门博客
    today_hot_data = savecache(get_today_hot_read_data,"today_hot_data", blog_content_type, 3600)  # 今日热门博客
    week_days_hot_data = savecache(get_7_days_hot_data,"week_days_hot_data", blog_content_type, 3600)  # 一周热门博客
    context = {
        "read_nums": read_nums,
        "read_nums_dates": read_nums_dates,
        "yesterday_hot_data": yesterday_hot_data,
        "today_hot_data": today_hot_data,
        "week_days_hot_data": week_days_hot_data,
    }
    return render(request, 'home.html', context)


def blog_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    # 获取提交过来时当前链接 如果没有则返回首页
    referer = request.META.get("HTTP_REFERER", reverse("home"))
    if user is not None:
        login(request, user)
        return redirect(referer)
    else:
        return render(request, "error.html", {"message": "用户名或密码不正确"})