#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/28/0028 12:31
# @Author  : Usher
# @Site    : 
# @File    : blog_tags.py
from ..models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count
#为了能够通过 {% get_recent_posts %} 的语法在模板中调用这个函数，必须按照 Django 的规定注册这个函数为模板标签
#首先导入 template 这个模块，然后实例化了一个 template.Library 类，并将函数 get_recent_posts 装饰为 register.simple_tag。这样就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了

register = template.Library()
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
#归档
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')
#分类
@register.simple_tag
def get_categories():
    #category_list = Category.objects.annotate(num_posts=Count('post'))
    #return Category.objects.all()
    ## Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
