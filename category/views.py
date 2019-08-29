from django.shortcuts import render
from .models import category

def index_view(request):
    categories = category.objects.all()
    return render(request, "categories.html", {"categories": categories})

def category_view(request, slug):
    categoryChoose = category.objects.get(slug=slug)
    return render(request, "categories.html", {"category": categoryChoose})
