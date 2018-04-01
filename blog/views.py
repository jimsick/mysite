from django.shortcuts import render_to_response, get_object_or_404
from .models import BlogType, Blog
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count


def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUM)  # 每5篇为一页
    page_num = request.GET.get("page", 1)  # 获取get传页数
    page_of_blogs = paginator.get_page(page_num)  # 获取具体一页的内容
    blog_types = BlogType.objects.annotate(blog_count=Count("blog"))
    blog_dates = Blog.objects.dates("created_time", "month", order="DESC")
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,\
                                       created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count
    """
        分页情况:
        总页数小于5：
        总页数大于5
            1、  1 2 3 4 5   属于前2页时显示5页
            2、  17 18 19 20 21     属于最后2页时显示5页
    """
    page_num = int(page_num)
    if page_num <= 3:
        # 小于等于前3个
        # 判断总页数
        if paginator.num_pages <= 5:
            page_range = [x for x in range(1, paginator.num_pages + 1)]
        else:
            page_range = [1, 2, 3, 4, 5, '...', paginator.num_pages]
    elif page_num >= paginator.num_pages - 2:
        # 小于最后两个
        page_range = [1, '...', paginator.num_pages - 4, paginator.num_pages - 3, paginator.num_pages - 2,
                      paginator.num_pages - 1, paginator.num_pages]
    else:
        # 2,3,4,5,6 不属于前2个也不属于后2个
        page_range = [page_num - 2, page_num - 1, page_num, page_num + 1, page_num + 2]
        page_range.insert(0, '...')
        page_range.insert(0, 1)
        page_range.append('...')
        page_range.append(paginator.num_pages)

    context = {
        "blogs": page_of_blogs.object_list,
        "page_of_blogs": page_of_blogs,
        "blog_types": blog_types,
        "page_range": page_range,
        "blog_dates": blog_dates_dict,
    }
    return context


"""博客列表"""
def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    return render_to_response("blog/blog_list.html", context)


"""根据博客类型查看博客"""
def blog_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)  # 取出对应类型
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)  # 取出对应类型的所有博客
    context = get_blog_list_common_data(request, blogs_all_list)
    context["blog_type"] = blog_type
    return render_to_response("blog/blog_with_type.html", context)


"""根据日期查看博客"""
def blog_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    return render_to_response("blog/blog_with_date.html", context)


"""博客文章"""
def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    # if not request.COOKIES.get("readed_%s_num" % blog_pk):
    #     blog.readed_num += 1
    #     blog.save()
    context["blog"] = blog
    context["previous_blog"] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context["next_blog"] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    response = render_to_response("blog/blog_detail.html", context)
    # response.set_cookie("readed_%s_num" % blog_pk, 'true')
    return response