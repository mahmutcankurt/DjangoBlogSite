from django.contrib import admin
from .models import Article


class adminArticle(admin.ModelAdmin):
    list_display = ["title", "releaseDate", "slug"]
    list_display_links = ["releaseDate"]
    list_filter = ["releaseDate"]
    search_fields = ["title", "content"]
    list_editable = ["title"]


admin.site.register(Article)


