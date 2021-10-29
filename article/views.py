from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import Article, Comment
from .forms import CreateTextForm, CommentForm
from django.contrib.auth.decorators import login_required


# View function for Articles.

def article_view(request, slug):
    articleView = Article.objects.get(slug=slug)

    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = articleView
        comment.save()
        comment_form = CommentForm()

    return render(request, "Articles/articleDetail.html", {"article": articleView, "form": comment_form})


# View function for Create Text.

@login_required(login_url='/users/login/')
def CreateText_view(request):
    form = CreateTextForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        articles = Article.objects.latest("article.id")

        return HttpResponseRedirect("/article/" + articles.slug)
    return render(request, "Articles/CreateText.html", {"form": form})


# View function for Comment Add.

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


