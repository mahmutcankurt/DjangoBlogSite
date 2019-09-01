from django.urls import path
from .views import article_view, CreateText_view

app_name = "article"

urlpatterns = [
    path('createText', CreateText_view, name='createText'),
    path('<str:slug>', article_view, name='articleDetail'),
]
