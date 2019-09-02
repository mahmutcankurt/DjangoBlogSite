from django.shortcuts import render
from article.models import Article
from category.models import category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home_view(request):
    articlesList = Article.objects.all()
    categories = category.objects.all()
    paginator = Paginator(articlesList, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, "index.html", {"articles": articles, "categories": categories})

def search_view(request):
    query = request.GET.get("query")
    texts = Article.objects.filter(title__contains=query)

    return render(request, "search.html", {"texts": texts})
