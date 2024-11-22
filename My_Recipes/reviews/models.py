from django.db import models

from My_Recipes.accounts.models import RecipesUser
from My_Recipes.recipes.models import Recipe
from My_Recipes.reviews.choices import RatingChoices


# Create your models here.

class RecipeReview(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(RecipesUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=RatingChoices.choices)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe', 'user')

    def __str__(self):
        return f"Review by {self.user} for {self.recipe.title}"
