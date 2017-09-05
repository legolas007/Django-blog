from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.在后台注册我们自己创建的几个模型，这样 Django Admin 才能知道它们的存在，
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'author']

# 把新增的 PostAdmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)