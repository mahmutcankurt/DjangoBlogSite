from django.shortcuts import render
from article.models import Article
from category.models import category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Home page views.

@login_required(login_url='/users/login/')
def home_view(request):
    articlesList = Article.objects.all()
    query = request.GET.get('query', None)
    categories = category.objects.all()
    paginator = Paginator(articlesList, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    if query:
        articles = articlesList.filter(Q(title__icontains=query) | Q(content__icontains=query))

    return render(request, "index.html", {"articles": articles, "categories": categories})


