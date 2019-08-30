from django.urls import path
from .views import article_view

app_name = "article"

urlpatterns =[
    path('<str:slug>', article_view),
]