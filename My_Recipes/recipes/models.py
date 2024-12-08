from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import Avg

from My_Recipes.accounts.models import RecipesUser
from My_Recipes.validators import IsItAlpha


class Recipe(models.Model):

    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3),
            IsItAlpha('Title should be only letters!'),
        ],
    )

    description = models.TextField(
        max_length=100,
    )

    prep_time = models.PositiveIntegerField(
        help_text="Preparation time in minutes...",
        validators=[MinValueValidator(1),
                    ]
    )

    cook_time = models.PositiveIntegerField(
        help_text="Cooking time in minutes...",
        validators=[
            MinValueValidator(1),],
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

    def total_time(self):
        return self.prep_time + self.cook_time

    def __str__(self):
        return self.title

    def get_average_rating(self):
        return self.recipe_reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']

    def reviews_count(self):
        return self.recipe_reviews.count()
