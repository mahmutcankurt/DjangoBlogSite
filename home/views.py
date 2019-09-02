from django.shortcuts import render
from article.models import Article
from category.models import category


def home_view(request):
    articles = Article.objects.all()
    categories = category.objects.all()
    return render(request, "index.html", {"articles": articles, "categories": categories})

def search_view(request):
    query = request.GET.get("query")
    texts = Article.objects.filter(title__contains=query)

    return render(request, "search.html", {"texts": texts})
