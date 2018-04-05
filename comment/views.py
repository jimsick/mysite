from django.shortcuts import render, reverse, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Comment

def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    user = request.user
    content_type = request.POST.get('content_type', '')
    object_id = int(request.POST.get('object_id'))
    text = request.POST.get('text', '')
    model_class = ContentType.objects.get(model=content_type).model_class()
    model_obj = model_class.objects.get(pk=object_id)

    comment = Comment()
    comment.content_object = model_obj
    comment.text = text
    comment.user = user
    comment.save()
    return redirect(referer)
