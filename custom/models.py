from django.db import models
from article.models import *
from category.models import *

from django.contrib.auth import get_user_model

import string
import random

# Create your models here.
User = get_user_model()

def unique_slug_generator(modelname, slug):
    def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
        return "".join(random.choice(chars) for _ in range(size))

    # if object with given slug is exist
    if qs_exist := modelname.objects.filter(slug=slug).exists():
        new_slug = f"{slug}-{random_string_generator(size=4)}"
    else:
        new_slug = slug

    return new_slug

class CustomAdminPageArticleModel(models.Model):
    authorized = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name="Authorized")
    category = models.ForeignKey(category, on_delete=models.CASCADE, unique=True)
    title = models.CharField(verbose_name="Title", max_length=255)
    article_id = models.IntegerField(verbose_name="Article ID")
    article = models.RichTextField(verbose_name="Article", null=False, blank=False)
    releaseDate = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(verbose_name="Slug", editable=False)

    class Meta: 
        verbose_name = "Custom Admin Panel Article"
        verbose_name_plural = "Custom Admin Panel Articles"
        
    def save(self, *args, **kwargs):
        s = f"{self.authorized}-{self.title}"
        uSlug = unique_slug_generator(CustomAdminPageArticleModel, s)
        self.slug = slugify(uSlug)
        super(CustomAdminPageArticleModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.authorized} - {self.title}"

    def get_absolute_url(self):
        return f"custom-admin-page-article-model/{self.slug}"


class CustomAdminPageCategoryModel(models.Model):    
    creator = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name="Creator")
    title = models.CharField(max_length=120, primary_key=True)
    slug = models.SlugField(unique=True, editable=False)
    

    class Meta: 
        verbose_name = "Custom Admin Panel Category"
        verbose_name_plural = "Custom Admin Panel Categories"
        
    def save(self, *args, **kwargs):
        s = f"{self.creator}-{self.title}"
        uSlug = unique_slug_generator(CustomAdminPageCategoryModel, s)
        self.slug = slugify(uSlug)
        super(CustomAdminPageCategoryModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.creator} - {self.title}"

    def get_absolute_url(self):
        return f"custom-admin-page-category-model/{self.slug}"


class CustomAdminPageCommentModel(models.Model):
    authorized = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name="Authorized")
    article = models.ForeignKey(Article, on_delete= models.CASCADE, verbose_name="Comment")
    text = models.TextField(max_length=600, verbose_name="Text")
    releaseDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Custom Admin Panel Comment"
        verbose_name_plural = "Custom Admin Panel Comments"
        ordering = ['-releaseDate']

    def __str__(self):
        return "%s - %s" % (self.article, self.authorized)


class Re_Turn(models.Model):
    authorized = models.ForeignKey(
        User, 
        on_delete= models.CASCADE, 
        verbose_name="Authorized"
    )
    
    customadminpagearticlemodel = models.ForeignKey(
        CustomAdminPageArticleModel,
        on_delete=models.CASCADE,
        related_name = "CustomAdminPageArticleModel",
        null=True,
        blank=True
    )
    
    customadminpagecategorymodel = models.ForeignKey(
        CustomAdminPageCategoryModel,
        on_delete=models.CASCADE,
        related_name = "CustomAdminPageCategoryModel",
        null=True,
        blank=True
    )
    
    customadminpagecommentmodel = models.ForeignKey(
        CustomAdminPageCategoryModel,
        on_delete=models.CASCADE,
        related_name = "CustomAdminPageCommentModel",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name="Re_Turn"
        verbose_name_plural="Re_Turns"

