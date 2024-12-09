from django.core.validators import MinLengthValidator
from django.db import models

from My_Recipes.ingredients.models import Ingredients
from My_Recipes.recipes.models import Recipe
from My_Recipes.validators import IsItAlpha


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
        max_length=6,
        validators=[
            MinLengthValidator(1),
        ]
    )

    measurement = models.CharField(
        max_length=20,
        validators=[IsItAlpha('Measurement value should be only letters!'),],
    )

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.title}"
