from django.urls import path
from .views import *

urlpatterns = [


    # articles

    path('admin-articles', CustomAdminPageArticleView.as_view(), name="admin-articles"),

    # categories

    path('admin-categories', CustomAdminPageCategoryView.as_view(), name="admin-categories"),

    # comments

    path('admin-comments', CustomAdminPageCommentView.as_view(), name="admin-comments"),
    

]