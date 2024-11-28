from django.db import models

from My_Recipes.accounts.models import RecipesUser


class Article(models.Model):

    category = models.CharField(
        max_length=50,
    )

    article_image = models.ImageField(
        upload_to='photos/article_pictures',
        blank=True,
        null=True,
    )

    title = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        max_length=100,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title
