from django.shortcuts import render_to_response, render, redirect, reverse
from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Sum
import datetime
from blog.models import Blog
from read_statistics.utils import (get_seven_days_read_data,
                                   get_yesterday_hot_read_data,
                                   get_today_hot_read_data,
                                   get_7_days_hot_data)

from .forms import LoginForm, RegForm
"""
    将数据保存到cache中
        func  方法名
        name  cache中对应的key
        blog_content_type
 """
def savecache(func, name, blog_content_type, time=60):

    result = cache.get(name)
    if not result:
        result = func(blog_content_type)
        cache.set(name, result, time)
    return result


"""首页"""
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


"""博客登录页面"""
def blog_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login(request, user=login_form.cleaned_data['user'])
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()
    content = {
        'login_form': login_form
    }
    return render(request, 'login.html', content)


"""博客注册页面"""
def blog_register(request):
    if request.method == "POST":
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password_again = reg_form.cleaned_data['password_again']
            try:
                user = User.objects.create_user(username, email, password_again)
                user.save()
                user_login = authenticate(username=username, password=password_again)
                login(request, user_login)
                return redirect(request.GET.get('from', reverse('home')))
            except Exception as e:
                print(e)
    else:
        reg_form = RegForm()
    content = {
        'reg_form': reg_form
    }
    return render(request, 'register.html', content)
