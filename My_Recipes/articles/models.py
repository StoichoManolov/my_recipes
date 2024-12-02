from django.db import models
from django.db.models import Avg

from My_Recipes.accounts.models import RecipesUser


class Article(models.Model):

    created_by = models.ForeignKey(
        RecipesUser,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    title = models.CharField(
        max_length=50,
    )

    article_image = models.ImageField(
        upload_to='photos/article_pictures',
        blank=True,
        null=True,
    )

    category = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        max_length=100,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

    def get_average_rating(self):
        return self.article_reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']

    def reviews_count(self):
        return self.article_reviews.count()
