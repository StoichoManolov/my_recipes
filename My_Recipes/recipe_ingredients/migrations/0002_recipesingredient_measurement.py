# Generated by Django 5.1.3 on 2024-11-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipesingredient',
            name='measurement',
            field=models.CharField(default='grams', max_length=50),
            preserve_default=False,
        ),
    ]
