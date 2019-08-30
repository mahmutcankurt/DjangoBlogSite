from django.shortcuts import render
from .models import Article


def article_view(request, slug):
    articleView = Article.objects.get(slug=slug)

    return render(request, "articleDetail.html", {"articleView": articleView})

