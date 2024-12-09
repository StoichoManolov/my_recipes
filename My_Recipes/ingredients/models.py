from django.core.validators import MinLengthValidator
from django.db import models

from My_Recipes.validators import IsItAlpha

# Create your models here.


class Ingredients(models.Model):
    name = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3),
            IsItAlpha('Ingredient name should be only letters!'),
        ]
    )

    def __str__(self):
        return self.name
