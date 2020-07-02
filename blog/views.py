from django.shortcuts import render
from blog.models import BlogPost
from .models import BlogArticles
from django.shortcuts import render, get_object_or_404


# Create your views here.
def archive(request):
    posts = BlogPost.objects.all()
    return render(request, 'archive.html', {'posts': posts})


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})


def blog_article(request, article_id):
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "blog/content.html", {"article": article, "publish": pub})