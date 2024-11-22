from django.db import models

from My_Recipes.accounts.models import RecipesUser


class Recipe(models.Model):

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField()

    prep_time = models.PositiveIntegerField(
        help_text="Preparation time in minutes",
    )

    cook_time = models.PositiveIntegerField(
        help_text="Cooking time in minutes",
    )

    instructions = models.TextField()

    image = models.ImageField(
        upload_to='photos/recipe_pictures/',
        blank=True,
        null=True,
    )

    created_by = models.ForeignKey(
        RecipesUser,
        on_delete=models.CASCADE,
        related_name='recipes_created',
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    approved = models.BooleanField(default=False)

    def total_time(self):
        return self.prep_time + self.cook_time

    def __str__(self):
        return self.title

