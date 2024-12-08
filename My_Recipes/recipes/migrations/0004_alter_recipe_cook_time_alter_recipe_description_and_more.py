# Generated by Django 5.1.3 on 2024-12-03 06:58

import My_Recipes.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_delete_recipes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.PositiveIntegerField(help_text='Cooking time in minutes...', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(help_text='Describe your recipe...', max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.PositiveIntegerField(help_text='Preparation time in minutes...', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(help_text='Title of the recipe...', max_length=100, validators=[django.core.validators.MinLengthValidator(3), My_Recipes.validators.IsItAlpha('Title should be only letters!')]),
        ),
    ]
