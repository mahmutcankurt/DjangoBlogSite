from django.shortcuts import render
from .models import category
from article.models import Article
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Categories index page views.

def index_view(request):
    categories = category.objects.all()

    return render(request, "categories.html", {"categories": categories})

# Category view.
def category_view(request, slug):
    categoryChoose = category.objects.get(slug=slug)
    articlesList = Article.objects.filter(category=categoryChoose)
    paginator = Paginator(articlesList, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, "categories.html", {"categorysecim": categoryChoose, "articles": articles})
