# Generated by Django 5.1.3 on 2024-11-29 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe_ingredients', '0001_initial'),
        ('recipes', '0002_remove_recipes_created_by_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipesingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredients', to='recipes.recipe'),
        ),
    ]
