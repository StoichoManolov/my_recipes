from django.db import models

from My_Recipes.accounts.models import RecipesUser
from My_Recipes.articles.models import Article
from My_Recipes.recipes.models import Recipe
from My_Recipes.reviews.choices import RatingChoices


# Create your models here.
class Reviews(models.Model):
    user = models.ForeignKey(RecipesUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=RatingChoices.choices)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class RecipeReview(Reviews):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_reviews')

    class Meta(Reviews.Meta):
        unique_together = ('recipe', 'user')

    def __str__(self):
        return f"Review by {self.user} for {self.recipe.title} with {self.rating}"


class ArticleReview(Reviews):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_reviews')

    class Meta(Reviews.Meta):
        unique_together = ('article', 'user')

    def __str__(self):
        return f"Review by {self.user} for {self.article.title} with {self.rating}"
