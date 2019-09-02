from django.shortcuts import render, HttpResponseRedirect
from .models import Article, Comment
from .forms import CreateTextForm


def article_view(request, slug):
    articleView = Article.objects.get(slug=slug)
    comments = Comment.objects.filter(text=articleView)

    return render(request, "Articles/articleDetail.html", {"article": articleView, "comments":comments})


def CreateText_view(request):
    form = CreateTextForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        articles = Article.objects.latest("id")

        return HttpResponseRedirect("/article/" + articles.slug)
    return render(request, "Articles/CreateText.html", {"form": form})

def addComment_view(request):
    text = request.GET.get("commentContent")
    articleId = request.GET.get("articleId")

    if text and articleId:
        articles = Article.objects.get(id=articleId)
        Comment.objects.create(text=text, writing=articles)

        return HttpResponseRedirect("/article/" + articles.slug)
    #return render(request, "Articles/articleDetail.html")
