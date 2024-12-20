# Generated by Django 5.1.3 on 2024-11-29 14:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
        ('recipes', '0003_delete_recipes'),
        ('reviews', '0003_remove_recipereview_review_articlereview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlereview',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='recipereview',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='articlereview',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_reviews', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='recipereview',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_reviews', to='recipes.recipe'),
        ),
    ]
