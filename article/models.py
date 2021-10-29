from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from category.models import category

# Model files of Article.

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = RichTextField(primary_key=True)
    releaseDate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name="articles", unique=True)
    like = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    # The slug function used to create a link.

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


# Comment model.
class Comment(models.Model):
    author = models.CharField(verbose_name='author', max_length=150)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments", verbose_name='Post', primary_key=True, unique=True)
    text = models.TextField(max_length=600, verbose_name='text')
    releaseDate = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering=['-releaseDate']

    def __str__(self):
        return "%s - %s" % (self.article, self.author)

