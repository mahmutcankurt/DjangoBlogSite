from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from category.models import category

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = RichTextField()
    releaseDate = models.DateTimeField(auto_now_add=True)
    image = models.FileField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        counter = 1

        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + str(counter)
            counter += 1

        return unique_slug
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Article, self).save(*args, **kwargs)

