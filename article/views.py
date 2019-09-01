from django.shortcuts import render, HttpResponseRedirect
from .models import Article
from .forms import CreateTextForm


def article_view(request, slug):
    articleView = Article.objects.get(slug=slug)

    return render(request, "Articles/articleDetail.html", {"article": articleView})


def CreateText_view(request):
    form = CreateTextForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        article = Article.objects.latest("id")

        return HttpResponseRedirect("/article/" + article.slug)
    return render(request, "Articles/CreateText.html", {"form": form})

