from django.shortcuts import render, get_object_or_404
from .models import Category, Tag, Article, Profile
from core.models import SiteSettings


def article_list(request):
    articles = Article.objects.filter(status='published')
    site_settings = SiteSettings.objects.first()
    context = {
        'articles': articles,
        'site_settings': site_settings
    }
    return render(request, 'blog/article_list.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    categories = Category.objects.all()
    latest_articles = Article.objects.filter(status='published').exclude(slug=article.slug).order_by('-created_at')[:3]
    popular_tags = Tag.objects.all().order_by('-views')[:8]
    site_settings = SiteSettings.objects.first()
    try:
        author_profile = Profile.objects.get(user=article.author)
    except Profile.DoesNotExist:
        author_profile = None

    context = {
        'article': article,
        'categories': categories,
        'latest_articles': latest_articles,
        'popular_tags': popular_tags,
        'author_profile': author_profile,
        'site_settings': site_settings
    }
    return render(request, 'blog/article_detail.html', context)



def category_article(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category)
    site_settings = SiteSettings.objects.first()
    context = {
        'category': category,
        'articles': articles,
        'site_settings': site_settings
    }
    return render(request, 'blog/category_article.html', context)


def tag_article(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    articles = tag.articles.all()
    site_settings = SiteSettings.objects.first()
    context = {
        'tag': tag,
        'articles': articles,
        'site_settings': site_settings
    }
    return render(request, 'blog/tag_article.html', context)


def search(request):
    articles_search = request.GET.get('search')
    articles = Article.objects.filter(status='published', title__icontains=articles_search)
    context = {
        'articles': articles
    }
    return render(request, 'blog/article_list.html', context)
