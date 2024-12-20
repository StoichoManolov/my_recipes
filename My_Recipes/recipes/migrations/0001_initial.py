# Generated by Django 5.1.3 on 2024-11-20 00:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prep_time', models.PositiveIntegerField(help_text='Preparation time in minutes')),
                ('cook_time', models.PositiveIntegerField(help_text='Cooking time in minutes')),
                ('instructions', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipe_pictures/')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
