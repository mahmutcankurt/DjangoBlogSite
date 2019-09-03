from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import Article, Comment
from .forms import CreateTextForm, CommentForm


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
    article = get_object_or_404(Article, id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = article
            comment.save()
            return redirect('articleDetail', pk=articleId)

        else:
            form = CommentForm()
        return render(request, 'Articles/articleDetail.html', {'form': form})

    #if text and articleId:
        #articles = Article.objects.get(id=articleId)
        #Comment.objects.create(text=text, writing=articles)

        #return HttpResponseRedirect("/article/" + articles.slug)
    #return render(request, "Articles/articleDetail.html")
