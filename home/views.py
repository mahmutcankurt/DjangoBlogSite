from django.shortcuts import render
from article.models import Article
from category.models import category


def home_view(request):
    articles = Article.objects.all()
    categories = category.objects.all()
    return render(request, "index.html", {"articles": articles, "categories": categories})

