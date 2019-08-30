from django.shortcuts import render
from .models import Article


def article_view(request, slug):
    writing = Article.objects.get(slug=slug)

    return render(request, "", {"writing": writing})

