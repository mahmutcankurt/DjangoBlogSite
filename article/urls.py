from django.urls import path
from .views import article_view, CreateText_view, addComment_view

app_name = "article"

urlpatterns = [
    path('createText', CreateText_view, name='createText'),
    path('addComment', addComment_view, name='addComment'),
    path('<str:slug>', article_view, name='articleDetail'),
]
