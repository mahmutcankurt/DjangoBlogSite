from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse
from django.views import generic
from datetime import datetime
from django.conf import settings

# Create your views here.

class CustomAdminPageView(generic.ListView):
    pass