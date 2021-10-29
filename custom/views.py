from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse
from django.views import generic
from datetime import datetime
from django.conf import settings

from article.models import *
from category.models import *
from users.models import *
from home.models import *

# Create your views here.

class CustomAdminPageArticleView(generic.ListView):
    model = CustomAdminPageArticleModel
    template_name = 'templates/custom/article.html'
    fields = "__all__"


class CustomAdminPageCategoryView(generic.ListView):
    model = CustomAdminPageArticleModel
    template_name = 'templates/custom/category.html'
    fields = "__all__"


class CustomAdminPageCommentView(generic.ListView):
    model = CustomAdminPageArticleModel
    template_name = 'templates/custom/comment.html'
    fields = "__all__"

