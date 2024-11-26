from django.db import models

from My_Recipes.ingredients.models import Ingredients
from My_Recipes.recipes.models import Recipe


# Create your models here.


class RecipesIngredient(models.Model):

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients'
    )

    ingredient = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE,
    )

    quantity = models.CharField(
        max_length=50,
    )

    measurement = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.title}"
