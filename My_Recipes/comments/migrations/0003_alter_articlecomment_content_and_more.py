# Generated by Django 5.1.3 on 2024-12-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipecomment',
            name='content',
            field=models.TextField(),
        ),
    ]
