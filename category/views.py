from django.shortcuts import render
from .models import category
from article.models import Article

def index_view(request):
    categories = category.objects.all()

    return render(request, "categories.html", {"categories": categories})

def category_view(request, slug):
    categoryChoose = category.objects.get(slug=slug)
    articles = Article.objects.filter(category=categoryChoose)
    return render(request, "categories.html", {"categorysecim": categoryChoose, "articles":articles})
