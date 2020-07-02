from django.contrib import admin
from blog.models import BlogPost
from .models import BlogArticles


class BlogPostAdmin(admin.ModelAdmin):
    # pk:����
    # ����list_display��ʾҪ��ʾ��Щ����
    list_display = ['pk', 'title', 'body', 'timestamp']


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"


# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogArticles, BlogArticlesAdmin)
