from django.shortcuts import render
from .models import Article
from .forms import CreateTextForm


def article_view(request, slug):
    articleView = Article.objects.get(slug=slug)

    return render(request, "Articles/articleDetail.html", {"article": articleView})


def CreateText_view(request):
    form = CreateTextForm(request.POST or None)

    return render(request, "Articles/CreateText.html", {"form": form})

