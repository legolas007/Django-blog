#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/4/0004 15:55
# @Author  : Usher
# @File    : feeds.py
from django.contrib.syndication.views import Feed
from .models import Post
class AllPostsRssFeed(Feed):
    title = "Django 博客"
    link = "/"
    description = "Rss订阅"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body

